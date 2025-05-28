from pathlib import Path

schema_text = """-- gtp.dbo.available_stock definition

-- Drop table

-- DROP TABLE gtp.dbo.available_stock;

CREATE TABLE gtp.dbo.available_stock (
	id bigint IDENTITY(1,1) NOT NULL,
	sku varchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NOT NULL,
	[source] varchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	created_timestamp datetime DEFAULT getdate() NOT NULL
);


-- gtp.dbo.cluster_status definition

-- Drop table

-- DROP TABLE gtp.dbo.cluster_status;

CREATE TABLE gtp.dbo.cluster_status (
	id tinyint NOT NULL,
	description varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT cluster_status_PK PRIMARY KEY (id)
);


-- gtp.dbo.cluster_type definition

-- Drop table

-- DROP TABLE gtp.dbo.cluster_type;

CREATE TABLE gtp.dbo.cluster_type (
	id varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	description varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT cluster_type_PK PRIMARY KEY (id)
);


-- gtp.dbo.compaction_tote_history definition

-- Drop table

-- DROP TABLE gtp.dbo.compaction_tote_history;

CREATE TABLE gtp.dbo.compaction_tote_history (
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[user] varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	id bigint IDENTITY(1,1) NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT compaction_tote_history_PK PRIMARY KEY (id)
);


-- gtp.dbo.compaction_transaction_history definition

-- Drop table

-- DROP TABLE gtp.dbo.compaction_transaction_history;

CREATE TABLE gtp.dbo.compaction_transaction_history (
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[user] varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[source] varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	destination varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL
);
 CREATE NONCLUSTERED INDEX IX_compaction_transaction_history_create_time_include_source ON gtp.dbo.compaction_transaction_history (  create_time ASC  )  
	 INCLUDE ( destination , sku , source ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.container_type definition

-- Drop table

-- DROP TABLE gtp.dbo.container_type;

CREATE TABLE gtp.dbo.container_type (
	id tinyint NOT NULL,
	value varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT container_type_PK PRIMARY KEY (id)
);


-- gtp.dbo.empty_carton_queue definition

-- Drop table

-- DROP TABLE gtp.dbo.empty_carton_queue;

CREATE TABLE gtp.dbo.empty_carton_queue (
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	processed tinyint NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT empty_carton_queue_PK PRIMARY KEY (container)
);


-- gtp.dbo.enum_scanner_description definition

-- Drop table

-- DROP TABLE gtp.dbo.enum_scanner_description;

CREATE TABLE gtp.dbo.enum_scanner_description (
	id int IDENTITY(1,1) NOT NULL,
	scanner varchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	description varchar(256) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
);
 CREATE NONCLUSTERED INDEX enum_scanner_description_scanner_IDX ON gtp.dbo.enum_scanner_description (  scanner ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.global_config definition

-- Drop table

-- DROP TABLE gtp.dbo.global_config;

CREATE TABLE gtp.dbo.global_config (
	id varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	value varchar(8) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime NOT NULL,
	CONSTRAINT global_config_PK PRIMARY KEY (id)
);


-- gtp.dbo.label definition

-- Drop table

-- DROP TABLE gtp.dbo.label;

CREATE TABLE gtp.dbo.label (
	id varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	print_string varchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	printer_type varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	CONSTRAINT label_PK PRIMARY KEY (id)
);


-- gtp.dbo.location_container definition

-- Drop table

-- DROP TABLE gtp.dbo.location_container;

CREATE TABLE gtp.dbo.location_container (
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	location varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	update_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT container_location_PK PRIMARY KEY (location)
);


-- gtp.dbo.material definition

-- Drop table

-- DROP TABLE gtp.dbo.material;

CREATE TABLE gtp.dbo.material (
	id bigint IDENTITY(1,1) NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT PK__material__3213E83F19573DAF PRIMARY KEY (id)
);
 CREATE NONCLUSTERED INDEX IX_material_sku ON gtp.dbo.material (  sku ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_material_sku_quantity ON gtp.dbo.material (  sku ASC  , quantity ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_material_id_include_quantity ON gtp.dbo.material (  id ASC  )  
	 INCLUDE ( quantity ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.material_transactions definition

-- Drop table

-- DROP TABLE gtp.dbo.material_transactions;

CREATE TABLE gtp.dbo.material_transactions (
	id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	operation_type varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[source] varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	destination varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	[user] varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	sub_cluster varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	CONSTRAINT material_transactions_PK PRIMARY KEY (id)
);
 CREATE NONCLUSTERED INDEX idx_material_transactions_create_time_include_station_quantity ON gtp.dbo.material_transactions (  create_time ASC  )  
	 INCLUDE ( quantity , station ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_material_transactions_operation_type_create_time ON gtp.dbo.material_transactions (  operation_type ASC  , create_time ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.measurement definition

-- Drop table

-- DROP TABLE gtp.dbo.measurement;

CREATE TABLE gtp.dbo.measurement (
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	quantity int NOT NULL,
	[length] int NOT NULL,
	width int NOT NULL,
	height int NOT NULL,
	weight int NOT NULL,
	create_time datetime DEFAULT getdate() NULL,
	CONSTRAINT PK__measurem__B0CB374D2AB3AF8C PRIMARY KEY (sku,quantity)
);


-- gtp.dbo.node_status definition

-- Drop table

-- DROP TABLE gtp.dbo.node_status;

CREATE TABLE gtp.dbo.node_status (
	id varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	is_full tinyint NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT node_status_PK PRIMARY KEY (id)
);


-- gtp.dbo.outbound_container_status definition

-- Drop table

-- DROP TABLE gtp.dbo.outbound_container_status;

CREATE TABLE gtp.dbo.outbound_container_status (
	id tinyint NOT NULL,
	description varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT outbound_container_status_PK PRIMARY KEY (id)
);


-- gtp.dbo.picking_discrepancy_header definition

-- Drop table

-- DROP TABLE gtp.dbo.picking_discrepancy_header;

CREATE TABLE gtp.dbo.picking_discrepancy_header (
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[source] varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[action] varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	station_full bit NOT NULL,
	success bit NOT NULL,
	id bigint IDENTITY(1,1) NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT picking_discrepancy_header_PK PRIMARY KEY (id)
);
 CREATE NONCLUSTERED INDEX idx_picking_discrepancy_header_action_container_create_time ON gtp.dbo.picking_discrepancy_header (  action ASC  , container ASC  , create_time ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX picking_discrepancy_header_station_IDX ON gtp.dbo.picking_discrepancy_header (  station ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.printer definition

-- Drop table

-- DROP TABLE gtp.dbo.printer;

CREATE TABLE gtp.dbo.printer (
	id varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	is_active tinyint NOT NULL,
	ip varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	port int NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	printer_type varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	CONSTRAINT printer_PK PRIMARY KEY (id)
);


-- gtp.dbo.product definition

-- Drop table

-- DROP TABLE gtp.dbo.product;

CREATE TABLE gtp.dbo.product (
	sku varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	item_description varchar(500) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	category varchar(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	product_type varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	launch_date datetime NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	update_time datetime DEFAULT getdate() NOT NULL,
	barcode varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT 'X' NOT NULL,
	image_url varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	unit int NULL,
	item_code varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);
 CREATE NONCLUSTERED INDEX IX_product_barcode ON gtp.dbo.product (  barcode ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_product_sku_category ON gtp.dbo.product (  sku ASC  , category ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.scanner_events definition

-- Drop table

-- DROP TABLE gtp.dbo.scanner_events;

CREATE TABLE gtp.dbo.scanner_events (
	id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[type] varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	scanner varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	container varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	decision int DEFAULT '0' NOT NULL,
	CONSTRAINT scanner_events_PK PRIMARY KEY (id)
);
 CREATE NONCLUSTERED INDEX idx_scanner_events_scanner_create_time__Include__container ON gtp.dbo.scanner_events (  scanner ASC  , create_time ASC  )  
	 INCLUDE ( container ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_scanner_events_scanner_decision_include_id_create_time ON gtp.dbo.scanner_events (  scanner ASC  , decision ASC  )  
	 INCLUDE ( create_time , id ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX scanner_events_container_IDX1 ON gtp.dbo.scanner_events (  container ASC  , scanner ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX scanner_events_create_time_IDX_1 ON gtp.dbo.scanner_events (  create_time ASC  , container ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX scanner_events_scanner_IDX ON gtp.dbo.scanner_events (  scanner ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.scanner_graph definition

-- Drop table

-- DROP TABLE gtp.dbo.scanner_graph;

CREATE TABLE gtp.dbo.scanner_graph (
	id int IDENTITY(1,1) NOT NULL,
	[source] varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	target varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	source_tag varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	CONSTRAINT PK__scanner___3213E83F6BE64303 PRIMARY KEY (id)
);


-- gtp.dbo.station definition

-- Drop table

-- DROP TABLE gtp.dbo.station;

CREATE TABLE gtp.dbo.station (
	id varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[type] varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	user_id varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	operation_type varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	active_status bit DEFAULT 0 NOT NULL,
	CONSTRAINT station_PK PRIMARY KEY (id)
);


-- gtp.dbo.station_events definition

-- Drop table

-- DROP TABLE gtp.dbo.station_events;

CREATE TABLE gtp.dbo.station_events (
	id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[type] varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	operation_type varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	[user] varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	CONSTRAINT station_events_PK PRIMARY KEY (id)
);
 CREATE NONCLUSTERED INDEX station_events_type_IDX_1 ON gtp.dbo.station_events (  type ASC  , station ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX station_events_type_IDX_5 ON gtp.dbo.station_events (  type ASC  , create_time ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.station_group definition

-- Drop table

-- DROP TABLE gtp.dbo.station_group;

CREATE TABLE gtp.dbo.station_group (
	station varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	group_id varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL
);


-- gtp.dbo.stock_check_tote_history definition

-- Drop table

-- DROP TABLE gtp.dbo.stock_check_tote_history;

CREATE TABLE gtp.dbo.stock_check_tote_history (
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[user] varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	id bigint IDENTITY(1,1) NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT stock_check_tote_history_PK PRIMARY KEY (id)
);


-- gtp.dbo.sub_cluster_status definition

-- Drop table

-- DROP TABLE gtp.dbo.sub_cluster_status;

CREATE TABLE gtp.dbo.sub_cluster_status (
	id tinyint NOT NULL,
	description varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT subcluster_status_PK PRIMARY KEY (id)
);


-- gtp.dbo.supply_history definition

-- Drop table

-- DROP TABLE gtp.dbo.supply_history;

CREATE TABLE gtp.dbo.supply_history (
	id bigint IDENTITY(1,1) NOT NULL,
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	operation_type varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	location varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	buffer_count int NOT NULL,
	promised_count int NOT NULL,
	total_skus int NOT NULL,
	total_quantity int NOT NULL,
	status tinyint NOT NULL,
	divert_time datetime DEFAULT getdate() NOT NULL,
	release_time datetime DEFAULT getdate() NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	[user] varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	picking_quantity int NULL,
	picking_skus int NULL,
	scan_time datetime NULL,
	CONSTRAINT supply_history_PK PRIMARY KEY (id)
);
 CREATE NONCLUSTERED INDEX idx_supply_history_status_create_time_Include_all ON gtp.dbo.supply_history (  status ASC  , create_time ASC  )  
	 INCLUDE ( buffer_count , container , divert_time , location , picking_quantity , picking_skus , promised_count , release_time , scan_time , station , total_quantity , total_skus , user ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.verification_events definition

-- Drop table

-- DROP TABLE gtp.dbo.verification_events;

CREATE TABLE gtp.dbo.verification_events (
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	operation_type varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[user] varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[type] varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	discrepancy_type varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL
);
 CREATE NONCLUSTERED INDEX IX_verification_events_type_discrepancy_type ON gtp.dbo.verification_events (  type ASC  , discrepancy_type ASC  )  
	 INCLUDE ( create_time ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_verification_events_container__Include__station_operation_type_user_type_discrepancy_type_create_time ON gtp.dbo.verification_events (  container ASC  )  
	 INCLUDE ( create_time , discrepancy_type , operation_type , station , type , user ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.cluster definition

-- Drop table

-- DROP TABLE gtp.dbo.cluster;

CREATE TABLE gtp.dbo.cluster (
	order_id varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	priority smallint NOT NULL,
	[type] varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	wave varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	allocation varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	status tinyint NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	is_pulled tinyint DEFAULT 0 NOT NULL,
	[source] varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT 'WES' NOT NULL,
	group_id varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	CONSTRAINT cluster_PK PRIMARY KEY (id),
	CONSTRAINT cluster_FK FOREIGN KEY ([type]) REFERENCES gtp.dbo.cluster_type(id),
	CONSTRAINT [cluster_FK_!] FOREIGN KEY (status) REFERENCES gtp.dbo.cluster_status(id)
);
 CREATE NONCLUSTERED INDEX IDX__cluster__status ON gtp.dbo.cluster (  status ASC  )  
	 INCLUDE ( allocation , order_id , priority , type , wave ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_cluster_allocation ON gtp.dbo.cluster (  allocation ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_cluster_status ON gtp.dbo.cluster (  status ASC  )  
	 INCLUDE ( allocation , is_pulled , order_id , priority , type , wave ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_cluster_status_inc ON gtp.dbo.cluster (  status ASC  )  
	 INCLUDE ( allocation , create_time , is_pulled , order_id , priority , type , wave ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_cluster_wave ON gtp.dbo.cluster (  wave ASC  )  
	 INCLUDE ( priority ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_cluster_order_id ON gtp.dbo.cluster (  order_id ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.compaction_material_history definition

-- Drop table

-- DROP TABLE gtp.dbo.compaction_material_history;

CREATE TABLE gtp.dbo.compaction_material_history (
	reference bigint NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT compaction_material_history_FK FOREIGN KEY (reference) REFERENCES gtp.dbo.compaction_tote_history(id)
);


-- gtp.dbo.configuration definition

-- Drop table

-- DROP TABLE gtp.dbo.configuration;

CREATE TABLE gtp.dbo.configuration (
	station varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	starting_order_size int NOT NULL,
	lower_bound int NOT NULL,
	create_time datetime NOT NULL,
	pulled_weight float NOT NULL,
	dissimilarity_weight float NOT NULL,
	max_subcluster_preempt int NOT NULL,
	max_promised_containers int NULL,
	carton_threshold int NULL,
	category varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	priority_weight float NOT NULL,
	pulled_sequence_weight float NOT NULL,
	consume_weight float NOT NULL,
	tote_limit int NOT NULL,
	eligible_tote_limit int NOT NULL,
	order_dissimilarity_weight float NOT NULL,
	group_similarity_weight float DEFAULT 0 NOT NULL,
	CONSTRAINT configuration_PK PRIMARY KEY (station),
	CONSTRAINT configuration_FK FOREIGN KEY (station) REFERENCES gtp.dbo.station(id)
);


-- gtp.dbo.container definition

-- Drop table

-- DROP TABLE gtp.dbo.container;

CREATE TABLE gtp.dbo.container (
	id varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[type] tinyint NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT container_PK PRIMARY KEY (id),
	CONSTRAINT container_FK FOREIGN KEY ([type]) REFERENCES gtp.dbo.container_type(id)
);
 CREATE NONCLUSTERED INDEX IX_container_type ON gtp.dbo.container (  type ASC  )  
	 INCLUDE ( create_time ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.container_hierarchy definition

-- Drop table

-- DROP TABLE gtp.dbo.container_hierarchy;

CREATE TABLE gtp.dbo.container_hierarchy (
	child varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	parent varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT container_hierarchy_PK PRIMARY KEY (child),
	CONSTRAINT container_hierarchy_FK FOREIGN KEY (child) REFERENCES gtp.dbo.container(id),
	CONSTRAINT container_hierarchy_FK_1 FOREIGN KEY (parent) REFERENCES gtp.dbo.container(id)
);


-- gtp.dbo.material_container definition

-- Drop table

-- DROP TABLE gtp.dbo.material_container;

CREATE TABLE gtp.dbo.material_container (
	material bigint NOT NULL,
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	update_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT PK__material__DEDA4344A0B491F7 PRIMARY KEY (material),
	CONSTRAINT FK__material___conta__3F466844 FOREIGN KEY (container) REFERENCES gtp.dbo.container(id),
	CONSTRAINT FK__material___mater__3E52440B FOREIGN KEY (material) REFERENCES gtp.dbo.material(id)
);
 CREATE NONCLUSTERED INDEX IX_material_container_container ON gtp.dbo.material_container (  container ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_material_container_container_include ON gtp.dbo.material_container (  container ASC  )  
	 INCLUDE ( create_time , update_time ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_material_container_create_time ON gtp.dbo.material_container (  create_time ASC  )  
	 INCLUDE ( container ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.outbound_container definition

-- Drop table

-- DROP TABLE gtp.dbo.outbound_container;

CREATE TABLE gtp.dbo.outbound_container (
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	status tinyint NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT tote_PK PRIMARY KEY (container),
	CONSTRAINT outbound_container_FK FOREIGN KEY (status) REFERENCES gtp.dbo.outbound_container_status(id),
	CONSTRAINT tote_FK FOREIGN KEY (container) REFERENCES gtp.dbo.container(id)
);
 CREATE NONCLUSTERED INDEX IX_outbound_container_status_create_time ON gtp.dbo.outbound_container (  status ASC  , create_time ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_outbound_container_container ON gtp.dbo.outbound_container (  container ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.picking_discrepancy_log definition

-- Drop table

-- DROP TABLE gtp.dbo.picking_discrepancy_log;

CREATE TABLE gtp.dbo.picking_discrepancy_log (
	reference bigint NOT NULL,
	order_index int NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	container varchar(200) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT picking_discrepancy_log_FK FOREIGN KEY (reference) REFERENCES gtp.dbo.picking_discrepancy_header(id)
);
 CREATE NONCLUSTERED INDEX picking_discrepancy_log_reference_IDX ON gtp.dbo.picking_discrepancy_log (  reference ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.stock_check_container_mapping definition

-- Drop table

-- DROP TABLE gtp.dbo.stock_check_container_mapping;

CREATE TABLE gtp.dbo.stock_check_container_mapping (
	container varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	material bigint NOT NULL,
	updated_quantity int NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT stock_check_container_mappin_PK PRIMARY KEY (container,material),
	CONSTRAINT stock_check_container_mappin_FK FOREIGN KEY (material) REFERENCES gtp.dbo.material(id)
);


-- gtp.dbo.stock_check_material_history definition

-- Drop table

-- DROP TABLE gtp.dbo.stock_check_material_history;

CREATE TABLE gtp.dbo.stock_check_material_history (
	reference bigint NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NOT NULL,
	[type] varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	system_quantity int NOT NULL,
	user_quantity int NOT NULL,
	CONSTRAINT stock_check_material_history_FK FOREIGN KEY (reference) REFERENCES gtp.dbo.stock_check_tote_history(id)
);


-- gtp.dbo.sub_cluster definition

-- Drop table

-- DROP TABLE gtp.dbo.sub_cluster;

CREATE TABLE gtp.dbo.sub_cluster (
	id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	cluster_id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	status tinyint NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	is_pulled tinyint DEFAULT 0 NOT NULL,
	CONSTRAINT sub_cluster_PK PRIMARY KEY (id),
	CONSTRAINT sub_cluster_FK FOREIGN KEY (status) REFERENCES gtp.dbo.sub_cluster_status(id),
	CONSTRAINT sub_cluster_FK_1 FOREIGN KEY (cluster_id) REFERENCES gtp.dbo.cluster(id)
);
 CREATE NONCLUSTERED INDEX IDX__sub_cluster__status ON gtp.dbo.sub_cluster (  status ASC  )  
	 INCLUDE ( cluster_id ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_sub_cluster_cluster_id ON gtp.dbo.sub_cluster (  cluster_id ASC  )  
	 INCLUDE ( status ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_sub_cluster_is_pulled_status ON gtp.dbo.sub_cluster (  is_pulled ASC  , status ASC  )  
	 INCLUDE ( cluster_id , create_time ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_sub_cluster_status ON gtp.dbo.sub_cluster (  status ASC  )  
	 INCLUDE ( cluster_id , is_pulled ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_sub_cluster_status_include_cluter_id_create_time ON gtp.dbo.sub_cluster (  status ASC  )  
	 INCLUDE ( cluster_id , create_time ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.sub_cluster_line definition

-- Drop table

-- DROP TABLE gtp.dbo.sub_cluster_line;

CREATE TABLE gtp.dbo.sub_cluster_line (
	sub_cluster_id varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	sku varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	storer varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	quantity int NOT NULL,
	fulfilled_quantity int DEFAULT 0 NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	update_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT sub_cluster_line_PK PRIMARY KEY (sub_cluster_id,sku),
	CONSTRAINT sub_cluster_line_FK FOREIGN KEY (sub_cluster_id) REFERENCES gtp.dbo.sub_cluster(id)
);
 CREATE NONCLUSTERED INDEX IX_sub_cluster_line_create_time ON gtp.dbo.sub_cluster_line (  create_time ASC  )  
	 INCLUDE ( fulfilled_quantity , quantity ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_sub_cluster_line_fulfilled_quantity ON gtp.dbo.sub_cluster_line (  fulfilled_quantity ASC  )  
	 INCLUDE ( create_time , quantity , storer ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX IX_sub_cluster_line_sku ON gtp.dbo.sub_cluster_line (  sku ASC  )  
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;
 CREATE NONCLUSTERED INDEX idx_sub_cluster_line_quantity_include_fulfilled_quantity ON gtp.dbo.sub_cluster_line (  quantity ASC  )  
	 INCLUDE ( fulfilled_quantity ) 
	 WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
	 ON [PRIMARY ] ;


-- gtp.dbo.supply_container definition

-- Drop table

-- DROP TABLE gtp.dbo.supply_container;

CREATE TABLE gtp.dbo.supply_container (
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[source] varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	active_status bit DEFAULT 0 NOT NULL,
	CONSTRAINT supply_container_PK PRIMARY KEY (container),
	CONSTRAINT supply_container_FK FOREIGN KEY (container) REFERENCES gtp.dbo.container(id)
);


-- gtp.dbo.user_material definition

-- Drop table

-- DROP TABLE gtp.dbo.user_material;

CREATE TABLE gtp.dbo.user_material (
	user_id varchar(32) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	sku varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	storer varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	material int NULL,
	CONSTRAINT user_material_PK PRIMARY KEY (user_id),
	CONSTRAINT user_material_FK FOREIGN KEY (user_id) REFERENCES gtp.dbo.user_material(user_id)
);


-- gtp.dbo.container_subcluster definition

-- Drop table

-- DROP TABLE gtp.dbo.container_subcluster;

CREATE TABLE gtp.dbo.container_subcluster (
	container varchar(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	subcluster varchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	create_time datetime DEFAULT getdate() NOT NULL,
	CONSTRAINT container_subcluster_PK PRIMARY KEY (subcluster),
	CONSTRAINT container_subcluster_UN UNIQUE (container),
	CONSTRAINT container_subcluster_FK FOREIGN KEY (container) REFERENCES gtp.dbo.container(id),
	CONSTRAINT container_subcluster_FK_1 FOREIGN KEY (subcluster) REFERENCES gtp.dbo.sub_cluster(id),
	CONSTRAINT container_subcluster_FK_3 FOREIGN KEY (subcluster) REFERENCES gtp.dbo.sub_cluster(id)
);
"""

schema_file_path = Path(r"C:\Users\VatsalyaBetala\Documents\NL2SQL\static_gtp_schema.sql")

# Saves the DDL - 
schema_file_path.write_text(schema_text)
print("Schema saved to:", schema_file_path)

