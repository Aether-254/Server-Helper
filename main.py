"""
Aether_254's Server Helper
@author: Aether_254
@version: 1.0
@date: 2024/10/14
@description: A simple helper for players playing my server.
@license: GPL-3.0
@copyright: (c) Aether_254 2024
@contact: 484029294@qq.com
@github: https://github.com/Aether-254
@repo: https://github.com/Aether-254/Server-Helper
@disclaimer: This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""

import noneprompt
import pathlib
import os
import json
import mcstatus
import logging
import wget
import rich
from rich.logging import RichHandler

FORMAT = "%(message)s"
LOGLEVEL = logging.INFO
logging.basicConfig(
    level=LOGLEVEL, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
if not pathlib.Path("Server-Helper").exists():
    os.mkdir("Server-Helper")

# Delect minecraft exists
if pathlib.Path(".minecraft").exists():
    pass
else:
    print("未检测到 Minecraft 安装, 请先安装 Minecraft.")
    logging.log(logging.WARN, "未检测到 Minecraft 安装!")
    exit(1)

if pathlib.Path(".minecraft/versions").exists():
    pass
else:
    print("未检测到 Minecraft 版本文件夹, 请先安装 Minecraft.")
    logging.log(logging.WARN, "未检测到 Minecraft 安装!")
    exit(1)

# Delect Version 1.21 Fabric 0.16.0 exists
# Read json
try:
    with open(pathlib.Path("Server-Helper/version_delector.json"), "r") as f2:
        delector_data = json.load(f2)
except FileNotFoundError:
    logging.log(logging.ERROR, "读取版本检测器失败! 找不到文件 version_delector.json")
    logging.log(logging.INFO, "尝试自动下载...")
    try:
        wget.download(url="https://raw.githubusercontent.com/Aether-254/Server-Helper/refs/heads/master/Server-Helper/version_delector.json", out="Server-Helper/version_delector.json")
    except Exception as e:
        logging.log(logging.CRITICAL, f"下载版本检测器失败! Expection: {e}")
        exit(1)
    else:
        logging.log(logging.INFO, "下载成功! 请重新运行程序...")
        exit(1)
except Exception as e:
    logging.log(logging.CRITICAL, f"读取版本检测器失败! Expection: {e}")
    exit(1)
logging.log(logging.INFO, "读取版本检测器成功!")

#with open(pathlib.Path("1.21_delector.json"), "r") as f3:
#    delector1210_data = json.load(f3)
#    logging.log(logging.INFO, "读取版本检测器成功!")

try:
    with open(pathlib.Path("Server-Helper/1.21_delector.json"), "r") as f3:
        delector1210_data = json.load(f3)
except FileNotFoundError:
    logging.log(logging.ERROR, "读取版本检测器失败! 找不到文件 1.21_delector.json")
    logging.log(logging.INFO, "尝试自动下载...")
    try:
        wget.download(url="https://raw.githubusercontent.com/Aether-254/Server-Helper/refs/heads/master/Server-Helper/1.21_delector.json", out="Server-Helper/1.21_delector.json")
    except Exception as e:
        logging.log(logging.CRITICAL, f"下载版本检测器失败! Expection: {e}")
        exit(1)
    else:
        logging.log(logging.INFO, "下载成功! 请重新运行程序...")
        exit(1)
except Exception as e:
    logging.log(logging.CRITICAL, f"读取版本检测器失败! Expection: {e}")
    exit(1)
logging.log(logging.INFO, "读取版本检测器成功!")

jdatalist = []

logging.log(logging.DEBUG, "开始检测版本...")

for i in os.listdir(pathlib.Path(".minecraft/versions/")):
    if pathlib.Path(f".minecraft/versions/{i}/{i}.json").exists():
        with open(pathlib.Path(f".minecraft/versions/{i}/{i}.json"), "r") as f:
            jdata = json.load(f)
            try:
                tester = jdata['id']
            except KeyError:
                try:
                    tester = jdata['inheritsFrom']
                except KeyError:
                    logging.log(logging.WARN, f"检测到无法读取的版本: {i}")
                else:
                    logging.log(logging.DEBUG, f"检测到版本: {i} 为 {jdata['inheritsFrom']}")
                    jdatalist.append(jdata)
            else:
                logging.log(logging.DEBUG, f"检测到版本: {i} 为 {jdata['id']}")
                jdatalist.append(jdata)

while 1:
    ans = noneprompt.ListPrompt(
        question="请选择功能：",
        choices=[
            noneprompt.Choice("1. 重新安装 Mods", "reinstall_mods"),
            noneprompt.Choice("2. 安装皮肤补丁", "skin_patcher"),
            noneprompt.Choice("3. 刷新", "reflush"),
            noneprompt.Choice("4. 退出", "exit"),
            noneprompt.Choice("============", "line disabled")
        ]
        ).prompt()
    if ans == 1:
        pass