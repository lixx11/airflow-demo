namespace py data_source

struct DataReply {
    1: double a,
    2: double b,
}

struct DataRequest {
    1: string name,
}


service DataSource {

   DataReply fetch_data(1:DataRequest request),

}
