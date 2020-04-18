namespace py data_source_rpc

struct UnversionedTable {
  1: string date,
  2: binary data,
}

struct VersionedTable {
  1: string date,
  2: binary data,
  3: double timestamp,
  4: string user='',
  5: string comment='',
  6: string sig_type='',
}

service DataSource {

  UnversionedTable read_stock_tick(1:string date),

  void write_stock_tick(1:UnversionedTable table),

  VersionedTable read_stock_daily(1:string date),

  void write_stock_daily(1:VersionedTable table),

  VersionedTable read_signal(1:string date, 2:string sig_type),

  void write_signal(1:VersionedTable table),

}
