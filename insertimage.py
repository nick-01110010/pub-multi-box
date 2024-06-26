import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(name, resolution, image, table):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "enb_multi_box"
    )

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO {table}
                          (name, resolution, image) VALUES (%s,%s,%s)"""

        binImage = convertToBinaryData(image)

        # Convert data into tuple format
        insert_blob_tuple = (name, resolution, binImage)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")