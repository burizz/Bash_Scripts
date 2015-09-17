import netsnmp

oid = netsnmp.Varbind('sysDescr')
result = netsnmp.snmpwalk(oid,
                      Version = 2,
                      DestHost = "localhost",
                      Community= "public")
                      
