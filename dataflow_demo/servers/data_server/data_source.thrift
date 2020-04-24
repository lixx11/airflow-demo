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

  UnversionedTable read_stock_tick(1:string token, 2:string date),

  bool write_stock_tick(1:string token, 2:UnversionedTable table),

  VersionedTable read_stock_daily(1:string token, 2:string date),

  bool write_stock_daily(1:string token, 2:VersionedTable table),

  VersionedTable read_signal(1:string token, 2:string date, 3:string sig_type),

  bool write_signal(1:string token, 2:VersionedTable table),

}
