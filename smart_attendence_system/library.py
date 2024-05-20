import face_recognition
import cv2
import csv
import os
import datetime
import numpy
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "charusat_students"
)

mycursor = mydb.cursor()