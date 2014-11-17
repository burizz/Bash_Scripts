

def total_conn_number(output_string):
    """ Get a string as input, find where in the string "total connections count is located" and display only the value for "Total number of connection: " with nothing after it. """

    total_connections = 'Total number of connections'
    delimiter_string = '('

    start_index = output_string.find(total_connections)
    end_index = output_string.find(delimiter_string, start_index)

    print output_string[start_index:end_index]
    
    
output_string = "['PoolManager name:JDBC/BOSSCS', 'PoolManager object:2082207303', 'Total number of connections: 1 (max/min 10/1, reap/unused/aged 180/1800/0, connectiontimeout/purge 180/EntirePool)', '(testConnection/inteval false/0, stuck timer/time/threshold 0/0/0, surge time/connections 0/-1)', 'Shared Connection information (shared partitions 200)', '  No shared connections', '', 'Free Connection information (free distribution table/partitions 5/1)', '  (0)(0)MCWrapper id 2a405b3a  Managed connection WSRdbManagedConnectionImpl@2112be64  State:STATE_ACTIVE_FREE', '', '  Total number of connection in free pool: 1', 'UnShared Connection information']"
total_conn_number(output_string)



#