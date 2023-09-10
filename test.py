import mysql.connector

# Thay thế các giá trị sau bằng thông tin của cơ sở dữ liệu RDS của bạn
host = 'localhost'
user = 'root'
password = '12345678'

try:
    # Kết nối tới cơ sở dữ liệu
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
    )

    if connection.is_connected():
        print("Kết nối thành công vào RDS MySQL")

        # Thực hiện các thao tác với cơ sở dữ liệu ở đây

except Exception as e:
    print(f"Lỗi kết nối: {e}")

mycursor = connection.cursor()

sql = "INSERT INTO world.city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)"
val = [
    ("Tung", "AFG", "Kabol", 94), 
    ("Trang", "AFG", "Kabol", 94), 
    ("Duong", "AFG", "Kabol", 94)
    ]

for i in range(len(val)):
    mycursor.execute(sql, val[i])

connection.commit()

print(mycursor.rowcount, "record inserted.")
