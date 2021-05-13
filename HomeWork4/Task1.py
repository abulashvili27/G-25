import sqlite3


class Canada:
    def __init__(self, province_or_territory, population, land_area):
        self.province_or_territory = province_or_territory
        self.population = population
        self.land_area = land_area

    def __str__(self):
        return f"Province or Territory - {self.province_or_territory}, Population - {self.population}, Land/Area - {self.land_area}"


def create_table(con):
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS density(province_or_teritory TEXT, population INTEGER, land_area REAL)")
    return cur


def insert_data_in_db(con):
    count = count_records_in_db(con, "density")
    if count != 0:
        return
    cur = con.cursor()

    cur.execute("INSERT INTO density VALUES ('Newfoundland and Labrador', 512930, 370501.69)")
    cur.execute("INSERT INTO density VALUES ('Prince Edward Island', 135294, 5684.39)")
    cur.execute("INSERT INTO density VALUES ('Nova Scotia', 908007, 52917.43)")
    cur.execute("INSERT INTO density VALUES ('New Brunswick', 729498, 71355.67)")
    cur.execute("INSERT INTO density VALUES ('Quebec', 7237479, 1357743.08)")
    cur.execute("INSERT INTO density VALUES ('Ontario', 11410046, 907655.59)")
    cur.execute("INSERT INTO density VALUES ('Manitoba', 1119583, 551937.87)")
    cur.execute("INSERT INTO density VALUES ('Saskatchewan', 978933, 586561.35)")
    cur.execute("INSERT INTO density VALUES ('Alberta', 2974807, 639987.12)")
    cur.execute("INSERT INTO density VALUES ('British Columbia', 3907738, 926492.48)")
    cur.execute("INSERT INTO density VALUES ('Yukon Territory', 28674, 474706.97)")
    cur.execute("INSERT INTO density VALUES ('Northwest Territory', 37360, 1141108.37)")
    cur.execute("INSERT INTO density VALUES ('Nunavut', 26745, 1925460.18)")
    con.commit()


def count_records_in_db(con, table_name):
    cur = con.cursor()
    cur.execute(f"SELECT count() FROM {table_name}")
    result = cur.fetchone()
    return result[0]


def all_data_write_in_file(con):
    result2 = []
    with open("all_data_file", "w") as f:
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM density"):
            result2.append(row)

        for element in result2:
            f.write(str(element) + "\n")

    f.close()


def load_data(con):
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM density"):
        print(Canada(row[0], row[1], row[2]))


def only_population(con):
    cur = con.cursor()
    for row in cur.execute("SELECT population FROM density"):
        print("Population - ", row)


def countries_less_than_1mp(con):
    result = []
    with open("lt 1m population", "w") as f:
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM density WHERE population between 0 AND 1000000"):
            result.append(row)

        for element in result:
            f.write(str(element) + "\n")

    f.close()


# ცუდი ფორმატით გამოაქვს ეს გამოსასწორებელი მაქვს რაღაც ურევს
def countries_less_than_1mp_output(con):
    result = []
    with open("lt 1m population", 'r') as f2:
        for line in f2.readlines():
            row = line.strip().split(",")
            result.append(row)

    f2.close()
    return result


def lt_1_or_gt_5(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM density where population < 1000000 or population > 5000000")
    return cur.fetchall()


def area_gt_200K(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM density where land_area > 200000")
    return cur.fetchall()


def main():
    connection = sqlite3.connect("census.db")
    create_table(connection)
    insert_data_in_db(connection)
    count_records_in_db(connection, "density")
    load_data(connection)
    only_population(connection)
    countries_less_than_1mp(connection)
    print(countries_less_than_1mp_output(connection))
    print(lt_1_or_gt_5(connection))
    print(area_gt_200K(connection))


if __name__ == '__main__':
    main()
