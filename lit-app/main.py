import streamlit as st
import numpy as np
import pandas as pd
from database.database import get_session
from database.orm.user.crud import read_users

session = get_session()
users = read_users(db=session)

st.write(users)
