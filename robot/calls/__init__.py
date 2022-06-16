from os import listdir, mkdir
from pyrogram import Client

from robot import config
from robot.calls.queues import clear, get, is_empty, put, task_done
from robot.calls import queues
from robot.calls.youtube import download
from robot.calls.calls import run, pytgcalls
from robot.calls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from robot.calls.convert import convert
