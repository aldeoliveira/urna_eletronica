class QueryHelper:
    @staticmethod
    def format_data_object(columns, values):
        data_object = []
        for row in values:
            row_dict = {}
            for i in range(len(columns)):
                row_dict.update({columns[i]: row[i]})
            data_object.append(row_dict)
        return data_object
