from elasticsearch import Elasticsearch
es = Elasticsearch()
es.snapshot.get_repository('my_backup') # configuration information
es.snapshot.status('my_backup') # currently running snapshots


all_snapshots = es.snapshot.get(repository = 'my_backup', snapshot = '_all')

