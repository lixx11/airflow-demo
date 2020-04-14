namespace py zs_signal

struct SignalReply {
    1: double sig,
}

struct SignalRequest {
    1: string name,
}


service Signal {

   SignalReply CalcSignal(1:SignalRequest request),

}
