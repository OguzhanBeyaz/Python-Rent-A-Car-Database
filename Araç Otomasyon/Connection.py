import sqlite3 as sql 


def main():

    try:
        db=sql.connect("Final/Arac_otomasyon.db")
        print("Bağlantı Kuruldu...")

    except:
        print("Bağlantı Kurulamadı...")

    finally:
        db.close()

if __name__ == "__main__":
 main()