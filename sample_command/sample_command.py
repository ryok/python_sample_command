#!/usr/local/opt/python/bin/python3.7
# -*- coding: utf-8 -*-
import re
import sys
from sample_command.sample_command import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
