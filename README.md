# cffex_ccpm
读取中国金融期货交易所-数据-成交持仓排名
按日期爬取所有类型产品下的数据，并保持到数据库
数据库为SQLServer
配置信息在config.ini文件

数据库结构：
CREATE TABLE [dbo].[utQHJYTJ](
	[OID] [bigint] NOT NULL,
	[FSRQ] [datetime] NULL,
	[XXLY] [varchar](100) NULL,
	[JZRQ] [datetime] NULL,
	[TJFS] [int] NULL,
	[TJQJ] [int] NULL,
	[SC] [int] NULL,
	[BDMS] [varchar](200) NULL,
	[PZID] [int] NULL,
	[XH] [int] NULL,
	[HYH] [varchar](100) NULL,
	[HYMC] [varchar](200) NULL,
	[HYID] [int] NULL,
	[CJL] [decimal](19, 4) NULL,
	[CJE] [money] NULL,
	[CCL] [decimal](19, 4) NULL,
	[ZJL] [decimal](19, 4) NULL,
	[BL] [decimal](19, 6) NULL,
	[GKBZ] [tinyint] NOT NULL,
	[XGRY] [int] NOT NULL,
	[XGRY2] [int] NOT NULL,
	[XGSJ] [datetime] NOT NULL,
	[FBSJ] [datetime] NULL,
	[SHBZ] [int] NULL,
	[SHRY] [int] NULL,
	[SHSJ] [datetime] NULL,
	[NID] [bigint] NOT NULL
) ON [PRIMARY]


目前问题：
打包.exe文件未成功
