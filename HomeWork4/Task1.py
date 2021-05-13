import sqlite3


class Canada:
    def __init__(self, province_or_territory, population, land_area):
        self.province_or_territory = province_or_territory
        self.population = population
        self.land_area = land_area

    def __str__(self):
        if self.province_or_territory == 0 and self.land_area == 0:

            return f"Population - {self.population}"
        else:
            return f"Province or Territory - {self.province_or_territory}, Population - {self.population}, Land/Area - {self.land_area}"


def create_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS density(province_or_teritory TEXT, population INTEGER, land_area REAL)")
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


def all_data_from_db(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM density")
    return cur.fetchall()


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
            f.write(element + "\n")

    f.close()


def main():
    connection = sqlite3.connect("census.db")
    create_table(connection)
    insert_data_in_db(connection)
    count_records_in_db(connection, "density")
    print(all_data_from_db(connection))
    # load_data(connection)
    # only_population(connection)
    countries_less_than_1mp(connection)


if __name__ == '__main__':
    main()
