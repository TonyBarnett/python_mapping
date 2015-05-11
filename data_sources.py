import mongoengine
import pymssql

mongoengine.
server = pymongo.MongoClient('10.10.20.37')


def read_from_sql(query, params, database):
   with pymssql.connect('localhost', 'sa', 'deter101!', database) as conn:
        with conn.cursor() as cursor:
            #  The star says you want a list of parameters for the format.
            cursor.execute(query if not params else query.format(*params))
            return cursor.fetchall()


def reuters_single_class():
    training_data_collection = server.Temp.ReutersDataPaul
    data = {str(x['_id']): x for x in training_data_collection.find() if not x['data_type_lewis'] == 'NOT-USED'}
    # laziness, x['target'] in this instance is guaranteed to be a single item list, hence [0]ing it.
    training_data = {_id: {'description': x['description'],
                           'target_class': x['target'][0],
                           '_id': _id}
                     for _id, x in data.items() if x['data_type_lewis'] == 'TRAIN'}

    validation_data = {_id: {'description': x['description'],
                             'target_class': x['target'][0],
                             '_id': _id}
                       for _id, x in data.items() if x['data_type_lewis'] == 'TEST'}