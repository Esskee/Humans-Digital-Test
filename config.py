

class basevars():

        host='hd-rds-interviewees-cluster.cluster-cxqp4co8nabg.eu-west-1.rds.amazonaws.com'
        user='interview_user'
        port = 5432
        password = '*9zng$kv#g>L[`>{6beX.}U,H&p^^!Vv'
        database='external_demos'
        sslmode = 'require'

        conn_string = f'host = {host}, user = {user}, port = {port}, password = {password}, sslmode = {sslmode}'
