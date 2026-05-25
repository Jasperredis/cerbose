# SPDX-License-Identifier: LGPL-3.0-or-later

# Cerbose v2.0.0 | made by jasperredis | LGPLv3 (see LICENSE)
# A simple Python library for making colourful, tagged terminal output, along with additional console features.
#
# LICENSE: LGPL v3 (View in LICENSE-LGPL file in library root or at <https://www.gnu.org/licenses/lgpl-3.0.html>)
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This library is distributed WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library. If not, see <https://www.gnu.org/licenses/>.

__version__ = "2.0.0"

# Libraries
import os
import json
import datetime as dt
from colorama import init
# Modules
from . import config
from .cprint import cprint, mprint, reset_align
from .cquery import cquery, cyn
from .cerbar import cerbar



