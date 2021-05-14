import sqlite3

DATA_FILE = "dataset2.csv"


class Consumers:
    def __init__(self, order_date, region, client, item, units, unit_cost, total):
        self.order_date = order_date
        self.region = region
        self.client = client
        self.item = item
        self.units = units
        self.unit_cost = unit_cost
        self.total = total

    def __str__(self):
        return f"Order date: {self.order_date}, Region: {self.region}, Client: {self.client}, Item: {self.item}, Units: {self.units}, Unit cost: {self.unit_cost}, Total: {self.total}"

    def to_insert(self, table_name):
        return f"INSERT INTO {table_name} values ('{self.order_date}', '{self.region}', '{self.client}', '{self.item}', '{self.units}', '{self.unit_cost}', '{self.total}')"


def create_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sales_data(order_date DATE, region TEXT, client TEXT, item TEXT,"
                " units INTEGER, unit_cost INTEGER, total INTEGER)")
    return cur


def load_data(con, f_name):
    result = []
    cur = con.cursor()
    with open(f_name, 'r') as f:
        for line in f.readlines():
            row = line.strip().split(",")
            tmp = Consumers(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            result.append(tmp)
    return result


def count_records_in_db(con, table_name):
    cur = con.cursor()
    cur.execute(f"SELECT count() FROM {table_name}")
    result = cur.fetchone()
    return result[0]


def insert_data_in_db(con, info):
    count = count_records_in_db(con, "sales_data")
    if count != 0:
        return
    cur = con.cursor()
    for i in info[1:]:
        cur.execute(i.to_insert("sales_data"))
    con.commit()


def client_by_units(con):
    result = []
    cur = con.cursor()
    for i in cur.execute("SELECT * FROM sales_data ORDER BY total desc").fetchone():
        result.append(i)
    return Consumers(result[0], result[1], result[2], result[3], result[4], result[5], result[6])


def high_sales_products(con):
    result = []
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM sales_data ORDER BY item desc").fetchone():
        result.append(row)
    return Consumers(result[0], result[1], result[2], result[3], result[4], result[5], result[6])


# def total_in_region(con):
#     result = []
#     cur = con.cursor()
#     for row in cur.execute("SELECT * FROM sales_data").fetchall():
#         result.append(row)


def avg_price(con):
    cur = con.cursor()
    cur.execute("SELECT sum(unit_cost) FROM sales_data")
    for i in cur.fetchone():
        return i/43


def total(con):
    cur = con.cursor()
    cur.execute("SELECT sum(total) FROM sales_data")
    for i in cur.fetchone():
        return i


def main():
    connection = sqlite3.connect("data.db")
    create_table(connection)
    data = load_data(connection, DATA_FILE)
    insert_data_in_db(connection, data)
    # total_in_region(connection)
    # print(client_by_units(connection))
    # print(high_sales_products(connection))
    # print(avg_price(connection))
    # print(total(connection))


if __name__ == '__main__':
    main()
