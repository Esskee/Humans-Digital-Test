import psycopg2


class basevars():
    conn = psycopg2.connect(
                    host="hd-rds-interviewees-cluster.cluster-cxqp4co8nabg.eu-west-1.rds.amazonaws.com",
                    database="external_demos",
                    port=5432,
                    user="interview_user",
                    password="zZu\\X3=,\+(?H\2>Tj\F*wML]=+ET9a",
                    sslmode='require')
