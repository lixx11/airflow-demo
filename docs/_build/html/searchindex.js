Search.setIndex({docnames:["dataflow_demo","dataflow_demo.clients","dataflow_demo.servers","dataflow_demo.servers.auth_server","dataflow_demo.servers.auth_server.auth_rpc","dataflow_demo.servers.data_server","dataflow_demo.servers.data_server.data_source_rpc","dataflow_demo.services","dataflow_demo.services.signal_service","dataflow_demo.services.signal_service.signal_rpc","index","modules"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":2,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["dataflow_demo.rst","dataflow_demo.clients.rst","dataflow_demo.servers.rst","dataflow_demo.servers.auth_server.rst","dataflow_demo.servers.auth_server.auth_rpc.rst","dataflow_demo.servers.data_server.rst","dataflow_demo.servers.data_server.data_source_rpc.rst","dataflow_demo.services.rst","dataflow_demo.services.signal_service.rst","dataflow_demo.services.signal_service.signal_rpc.rst","index.rst","modules.rst"],objects:{"":{dataflow_demo:[0,0,0,"-"]},"dataflow_demo.clients":{auth_api:[1,0,0,"-"],base_api:[1,0,0,"-"],data_api:[1,0,0,"-"],signal_api:[1,0,0,"-"]},"dataflow_demo.clients.auth_api":{AuthAPI:[1,1,1,""]},"dataflow_demo.clients.auth_api.AuthAPI":{authenticate:[1,2,1,""],close:[1,2,1,""],has_perm:[1,2,1,""]},"dataflow_demo.clients.base_api":{BaseAPI:[1,1,1,""]},"dataflow_demo.clients.base_api.BaseAPI":{authenticate:[1,2,1,""],close:[1,2,1,""],is_login:[1,2,1,""]},"dataflow_demo.clients.data_api":{DataAPI:[1,1,1,""]},"dataflow_demo.clients.data_api.DataAPI":{read_signal:[1,2,1,""],read_stock_daily:[1,2,1,""],read_stock_tick:[1,2,1,""],write_signal:[1,2,1,""],write_stock_daily:[1,2,1,""],write_stock_tick:[1,2,1,""]},"dataflow_demo.clients.signal_api":{SignalAPI:[1,1,1,""]},"dataflow_demo.clients.signal_api.SignalAPI":{calc_signal:[1,2,1,""]},"dataflow_demo.servers":{auth_server:[3,0,0,"-"],data_server:[5,0,0,"-"]},"dataflow_demo.servers.auth_server":{auth_client:[3,0,0,"-"],auth_rpc:[4,0,0,"-"],auth_server:[3,0,0,"-"]},"dataflow_demo.servers.auth_server.auth_client":{main:[3,3,1,""]},"dataflow_demo.servers.auth_server.auth_rpc":{Auth:[4,0,0,"-"],constants:[4,0,0,"-"],ttypes:[4,0,0,"-"]},"dataflow_demo.servers.auth_server.auth_rpc.Auth":{Client:[4,1,1,""],Iface:[4,1,1,""],Processor:[4,1,1,""],authenticate_args:[4,1,1,""],authenticate_result:[4,1,1,""],has_perm_args:[4,1,1,""],has_perm_result:[4,1,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.Client":{authenticate:[4,2,1,""],has_perm:[4,2,1,""],recv_authenticate:[4,2,1,""],recv_has_perm:[4,2,1,""],send_authenticate:[4,2,1,""],send_has_perm:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.Iface":{authenticate:[4,2,1,""],has_perm:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.Processor":{process:[4,2,1,""],process_authenticate:[4,2,1,""],process_has_perm:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.authenticate_args":{read:[4,2,1,""],thrift_spec:[4,4,1,""],validate:[4,2,1,""],write:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.authenticate_result":{read:[4,2,1,""],thrift_spec:[4,4,1,""],validate:[4,2,1,""],write:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.has_perm_args":{read:[4,2,1,""],thrift_spec:[4,4,1,""],validate:[4,2,1,""],write:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_rpc.Auth.has_perm_result":{read:[4,2,1,""],thrift_spec:[4,4,1,""],validate:[4,2,1,""],write:[4,2,1,""]},"dataflow_demo.servers.auth_server.auth_server":{AuthServer:[3,1,1,""]},"dataflow_demo.servers.auth_server.auth_server.AuthServer":{Handler:[3,1,1,""],close:[3,2,1,""],serve:[3,2,1,""]},"dataflow_demo.servers.auth_server.auth_server.AuthServer.Handler":{authenticate:[3,2,1,""],has_perm:[3,2,1,""]},"dataflow_demo.servers.data_server":{data_client:[5,0,0,"-"],data_server:[5,0,0,"-"],data_source_rpc:[6,0,0,"-"],utils:[5,0,0,"-"]},"dataflow_demo.servers.data_server.data_client":{main:[5,3,1,""]},"dataflow_demo.servers.data_server.data_server":{DataServer:[5,1,1,""]},"dataflow_demo.servers.data_server.data_server.DataServer":{Handler:[5,1,1,""],close:[5,2,1,""],serve:[5,2,1,""]},"dataflow_demo.servers.data_server.data_server.DataServer.Handler":{read_signal:[5,2,1,""],read_stock_daily:[5,2,1,""],read_stock_tick:[5,2,1,""],write_signal:[5,2,1,""],write_stock_daily:[5,2,1,""],write_stock_tick:[5,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc":{DataSource:[6,0,0,"-"],constants:[6,0,0,"-"],ttypes:[6,0,0,"-"]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource":{Client:[6,1,1,""],Iface:[6,1,1,""],Processor:[6,1,1,""],read_signal_args:[6,1,1,""],read_signal_result:[6,1,1,""],read_stock_daily_args:[6,1,1,""],read_stock_daily_result:[6,1,1,""],read_stock_tick_args:[6,1,1,""],read_stock_tick_result:[6,1,1,""],write_signal_args:[6,1,1,""],write_signal_result:[6,1,1,""],write_stock_daily_args:[6,1,1,""],write_stock_daily_result:[6,1,1,""],write_stock_tick_args:[6,1,1,""],write_stock_tick_result:[6,1,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.Client":{read_signal:[6,2,1,""],read_stock_daily:[6,2,1,""],read_stock_tick:[6,2,1,""],recv_read_signal:[6,2,1,""],recv_read_stock_daily:[6,2,1,""],recv_read_stock_tick:[6,2,1,""],recv_write_signal:[6,2,1,""],recv_write_stock_daily:[6,2,1,""],recv_write_stock_tick:[6,2,1,""],send_read_signal:[6,2,1,""],send_read_stock_daily:[6,2,1,""],send_read_stock_tick:[6,2,1,""],send_write_signal:[6,2,1,""],send_write_stock_daily:[6,2,1,""],send_write_stock_tick:[6,2,1,""],write_signal:[6,2,1,""],write_stock_daily:[6,2,1,""],write_stock_tick:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.Iface":{read_signal:[6,2,1,""],read_stock_daily:[6,2,1,""],read_stock_tick:[6,2,1,""],write_signal:[6,2,1,""],write_stock_daily:[6,2,1,""],write_stock_tick:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.Processor":{process:[6,2,1,""],process_read_signal:[6,2,1,""],process_read_stock_daily:[6,2,1,""],process_read_stock_tick:[6,2,1,""],process_write_signal:[6,2,1,""],process_write_stock_daily:[6,2,1,""],process_write_stock_tick:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.read_signal_args":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.read_signal_result":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.read_stock_daily_args":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.read_stock_daily_result":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.read_stock_tick_args":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.read_stock_tick_result":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.write_signal_args":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.write_signal_result":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.write_stock_daily_args":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.write_stock_daily_result":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.write_stock_tick_args":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.DataSource.write_stock_tick_result":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.ttypes":{UnversionedTable:[6,1,1,""],VersionedTable:[6,1,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.ttypes.UnversionedTable":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.data_source_rpc.ttypes.VersionedTable":{read:[6,2,1,""],thrift_spec:[6,4,1,""],validate:[6,2,1,""],write:[6,2,1,""]},"dataflow_demo.servers.data_server.utils":{init_db:[5,3,1,""]},"dataflow_demo.services":{base_service:[7,0,0,"-"],signal_service:[8,0,0,"-"]},"dataflow_demo.services.base_service":{BaseService:[7,1,1,""]},"dataflow_demo.services.base_service.BaseService":{login_data_server:[7,2,1,""]},"dataflow_demo.services.signal_service":{signal_client:[8,0,0,"-"],signal_rpc:[9,0,0,"-"],signal_service:[8,0,0,"-"]},"dataflow_demo.services.signal_service.signal_client":{main:[8,3,1,""]},"dataflow_demo.services.signal_service.signal_rpc":{Signal:[9,0,0,"-"],constants:[9,0,0,"-"],ttypes:[9,0,0,"-"]},"dataflow_demo.services.signal_service.signal_rpc.Signal":{Client:[9,1,1,""],Iface:[9,1,1,""],Processor:[9,1,1,""],calc_signal_args:[9,1,1,""],calc_signal_result:[9,1,1,""]},"dataflow_demo.services.signal_service.signal_rpc.Signal.Client":{calc_signal:[9,2,1,""],recv_calc_signal:[9,2,1,""],send_calc_signal:[9,2,1,""]},"dataflow_demo.services.signal_service.signal_rpc.Signal.Iface":{calc_signal:[9,2,1,""]},"dataflow_demo.services.signal_service.signal_rpc.Signal.Processor":{process:[9,2,1,""],process_calc_signal:[9,2,1,""]},"dataflow_demo.services.signal_service.signal_rpc.Signal.calc_signal_args":{read:[9,2,1,""],thrift_spec:[9,4,1,""],validate:[9,2,1,""],write:[9,2,1,""]},"dataflow_demo.services.signal_service.signal_rpc.Signal.calc_signal_result":{read:[9,2,1,""],thrift_spec:[9,4,1,""],validate:[9,2,1,""],write:[9,2,1,""]},"dataflow_demo.services.signal_service.signal_service":{SignalService:[8,1,1,""]},"dataflow_demo.services.signal_service.signal_service.SignalService":{Handler:[8,1,1,""],serve:[8,2,1,""]},"dataflow_demo.services.signal_service.signal_service.SignalService.Handler":{calc_signal:[8,2,1,""]},"dataflow_demo.utils":{NotLoginError:[0,5,1,""],build_dummy_daily_table:[0,3,1,""],build_dummy_signal_table:[0,3,1,""],build_dummy_tick_table:[0,3,1,""],check_login:[0,3,1,""],check_perm:[0,3,1,""],check_rpc:[0,3,1,""],module_level_variable1:[0,4,1,""]},dataflow_demo:{clients:[1,0,0,"-"],servers:[2,0,0,"-"],services:[7,0,0,"-"],utils:[0,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"],"4":["py","attribute","Python attribute"],"5":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function","4":"py:attribute","5":"py:exception"},terms:{"\u4e0a\u6d77":1,"\u4e70\u4ef7":1,"\u5356\u4ef7":1,"\u6210\u4ea4\u91cf":1,"\u65e5\u671f":1,"\u6700\u65b0\u4ef7\u683c":1,"\u6df1\u5733":1,"\u80a1\u7968\u4ee3\u7801":1,"break":0,"class":[1,3,4,5,6,7,8,9],"function":0,"int":[0,1],"new":0,"return":[0,1],The:[0,4,6,9],accept:0,also:0,ani:0,anytim:0,api:[1,3,4],askpric:1,attribut:0,auth:[2,3],auth_api:[0,5,10,11],auth_client:[0,2],auth_fil:3,auth_host:1,auth_port:1,auth_rpc:[2,3],auth_serv:[0,2],authapi:1,authent:[1,3,4],authenticate_arg:4,authenticate_result:4,authserv:3,base:[0,1,3,4,5,6,7,8,9],base_api:[0,10,11],base_servic:[0,8,10,11],baseapi:1,baseservic:[7,8],behvaior:[4,6,9],bidpric:1,binari:[6,9],blank:0,block:0,bodi:0,build_dummy_daily_t:0,build_dummy_signal_t:0,build_dummy_tick_t:0,calc_sign:[1,8,9],calc_signal_arg:9,calc_signal_result:9,can:0,check_login:0,check_perm:0,check_rpc:0,choos:0,client:[0,4,6,9,10,11],close:[1,3,5],code:1,column:1,comment:[1,6,8,9],commit:[1,8,9],conf_fil:[3,5,7,8],consist:0,constant:[2,3,5,7,8],content:[10,11],convent:0,correct:[4,6,9],creat:0,data:[1,6],data_api:[0,8,10,11],data_cli:[0,2],data_host:1,data_port:1,data_serv:[0,2],data_source_rpc:[2,5],dataapi:1,datafram:1,dataserv:5,datasourc:[2,5],date:[1,5,6,8,9],datetim:1,db_conf:5,defin:1,demonstr:0,descript:1,dfdsafdsafdsaf:0,docstr:0,doctest:0,document:0,doubl:1,dsa:0,either:0,equal:0,exampl:[0,1],example_numpi:0,except:0,extend:0,fals:[1,8],fdsafdsaf:0,follow:0,form:0,format:[0,1],from:0,func:0,gener:0,given:0,handler:[3,4,5,6,8,9],has_perm:[1,3,4],has_perm_arg:4,has_perm_result:4,have:[0,4,6,9],header:0,help:0,host:1,how:0,howto:0,ifac:[4,6,9],illustr:0,immedi:0,implicitli:0,includ:0,indent:0,index:1,init_db:5,inlin:0,instead:0,invok:[4,6,9],iprot:[4,6,9],is_login:1,jfdkslkafdj:0,lastpric:1,length:0,level:0,like:0,limit:0,line:0,liter:0,login_data_serv:7,mai:0,main:[3,5,8],mg_db:5,mix:0,modul:[10,11],module_level_variable1:0,multipl:0,my_db:5,name:1,next:0,none:[1,4,6,9],normal:[4,6,9],note:[0,1],notloginerror:0,number:0,numpi:0,object:[1,3,4,5,6,7,8,9],one:0,oprot:[4,6,9],other:0,out:0,over:0,packag:[10,11],paramet:[0,1,4,6,9],password:[1,3,4,7],port:1,process:[4,6,9],process_authent:4,process_calc_sign:9,process_has_perm:4,process_read_sign:6,process_read_stock_daili:6,process_read_stock_tick:6,process_write_sign:6,process_write_stock_daili:6,process_write_stock_tick:6,processor:[4,6,9],python:0,rang:0,read:[4,6,9],read_sign:[1,5,6],read_signal_arg:6,read_signal_result:6,read_stock_daili:[1,5,6],read_stock_daily_arg:6,read_stock_daily_result:6,read_stock_tick:[1,5,6],read_stock_tick_arg:6,read_stock_tick_result:6,recv_authent:4,recv_calc_sign:9,recv_has_perm:4,recv_read_sign:6,recv_read_stock_daili:6,recv_read_stock_tick:6,recv_write_sign:6,recv_write_stock_daili:6,recv_write_stock_tick:6,request:[4,6,9],respons:[4,6,9],restructuredtext:0,resum:0,saf:0,safdsaf:0,section:[0,1],send_authent:4,send_calc_sign:9,send_has_perm:4,send_read_sign:6,send_read_stock_daili:6,send_read_stock_tick:6,send_write_sign:6,send_write_stock_daili:6,send_write_stock_tick:6,seqid:[4,6,9],serv:[3,5,8],server:[0,1,9,10,11],servic:[0,10,11],should:0,sig_typ:[1,5,6],signal:[7,8],signal_api:[0,10,11],signal_cli:[0,7],signal_rpc:[7,8],signal_servic:[0,7],signalapi:1,signalservic:8,specifi:0,sse:1,stand:0,start:0,stock:1,str:1,string:1,style:0,submodul:[2,10,11],subpackag:[10,11],success:[4,6,9],support:0,surround:0,sze:1,tabl:[5,6],text:0,thi:0,thrift:[4,6,9],thrift_spec:[4,6,9],tick:1,timestamp:6,token:[1,3,4,5,6],tprocessor:[4,6,9],ttype:[2,3,5,7,8],two:0,type:[0,1],underlin:0,unind:0,unversionedt:6,upper:0,use:0,user:6,usernam:[1,3,4,7],using:0,utf8:[4,6,9],util:[2,10,11],valid:[4,6,9],variabl:0,versionedt:6,volum:1,write:[1,4,6,9],write_sign:[1,5,6],write_signal_arg:6,write_signal_result:6,write_stock_daili:[1,5,6],write_stock_daily_arg:6,write_stock_daily_result:6,write_stock_tick:[1,5,6],write_stock_tick_arg:6,write_stock_tick_result:6,written:0,yield:0},titles:["dataflow_demo package","dataflow_demo.clients package","dataflow_demo.servers package","dataflow_demo.servers.auth_server package","dataflow_demo.servers.auth_server.auth_rpc package","dataflow_demo.servers.data_server package","dataflow_demo.servers.data_server.data_source_rpc package","dataflow_demo.services package","dataflow_demo.services.signal_service package","dataflow_demo.services.signal_service.signal_rpc package","dataflow_demo","dataflow_demo"],titleterms:{auth:4,auth_api:1,auth_client:3,auth_rpc:4,auth_serv:[3,4],base_api:1,base_servic:7,client:1,constant:[4,6,9],content:[0,1,2,3,4,5,6,7,8,9],data_api:1,data_cli:5,data_serv:[5,6],data_source_rpc:6,dataflow_demo:[0,1,2,3,4,5,6,7,8,9,10,11],datasourc:6,modul:[0,1,2,3,4,5,6,7,8,9],packag:[0,1,2,3,4,5,6,7,8,9],server:[2,3,4,5,6],servic:[7,8,9],signal:9,signal_api:1,signal_cli:8,signal_rpc:9,signal_servic:[8,9],submodul:[0,1,3,4,5,6,7,8,9],subpackag:[0,2,3,5,7,8],ttype:[4,6,9],util:[0,5]}})