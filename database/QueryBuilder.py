from .DataBase import DataBase
from .QueryHelper import QueryHelper


class QueryBuilder:

    def count_all(self, table_name):
        count = self.query_count(table_name, None)
        return count

    def count_where(self, table_name, dict_conditions):
        text_where_clause = self.where_clause(dict_conditions)
        count = self.query_count(table_name, text_where_clause)
        return count

    def where_clause(self, dict_conditions):
        # dict_conditions = {"column_condition_1": "value_condition_1", "columns_condition_2": "value_condition_2", ...}
        columns = list(dict_conditions.keys())
        text_clauses = []
        # text_clauses = ["column_condition_1 = value_condition_1",
        #                 "column_condition_2 = value_condition_2", ...]
        for column in columns:
            text_clauses.append("{0} = '{1}'".format(column, dict_conditions[column]))
        text_where_clause = " WHERE " + " AND ".join(text_clauses)
        # text_where_clause = " WHERE column_condition_1 = value_condition_1 AND
        #                             column_condition_2 = value_condition_2 ..."
        return text_where_clause

    def query_count(self, table_name, where_clause):
        text_query_count = "COUNT (*)"
        database_cursor = self.query_select(text_query_count, table_name, where_clause)
        result = database_cursor.fetchall()
        count = result[0][0]
        return count

    def select_all(self, table_name, columns):
        result_tup = self.query_select(columns, table_name, None)
        result_dict = self.format_tup_to_dict(result_tup)
        return result_dict

    def select_where(self, table_name, columns, dict_conditions):
        text_where_clause = self.where_clause(dict_conditions)
        result_tup = self.query_select(columns, table_name, text_where_clause)
        result_dict = self.format_tup_to_dict(result_tup)
        return result_dict

    def query_select(self, columns, table_name, where_clause):
        if not where_clause:
            where_clause = ""
        text_query_select = "SELECT {0} FROM {1}{2}".format(columns, table_name, where_clause)
        database = DataBase()
        database_connection = database.connect()
        database_cursor = database_connection.cursor()
        database_cursor.execute(text_query_select)
        result_tup = database_cursor
        return result_tup

    def format_tup_to_dict(self, database_cursor):
        queryhelper = QueryHelper
        col_names = []
        for column in database_cursor.description:
            col_names.append(column[0])
        selected_itens = queryhelper.format_data_object(col_names, database_cursor.fetchall())
        return selected_itens

    def delete_all(self, table_name):
        self.query_delete(table_name, None)

    def delete_where(self, table_name, dict_conditions):
        text_where_clause = self.where_clause(dict_conditions)
        self.query_delete(table_name, text_where_clause)

    def query_delete(self, table_name, text_where_clause):
        if not text_where_clause:
            text_where_clause = ""
        text_query_delete = "DELETE FROM {0}{1}".format(table_name, text_where_clause)
        database = DataBase()
        database_connect = database.connect()
        database_connect.cursor().execute(text_query_delete)
        database_connect.commit()

    def insert(self, table_name, entity_dict):
        text_columns = ",".join(list(entity_dict.keys()))
        text_values = entity_dict.values()
        spaces_text_values = "%s," * (len(text_values) - 1) + "%s"
        text_query_insert = "INSERT INTO {0} ({1}) VALUES ({2})".format(table_name, text_columns, spaces_text_values)
        database = DataBase()
        database_connection = database.connect()
        database_connection.cursor().execute(text_query_insert, tuple(text_values))
        database_connection.commit()
