__path__ = ["danielsdatastructures", "danielsdatastructures/queues"]

import os
cwd = os.getcwd()
import sys
sys.path.append(cwd+"/queues")

from danielsdatastructures.queues import Queue, CircularQueue 