namespace py auth_rpc


service Auth {

  string authenticate(1:string username, 2:string password),

  bool has_perm(1:string token, 2:string api),

}
