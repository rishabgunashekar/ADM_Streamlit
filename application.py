#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:05:50 2021

@author: rishab
"""


#Importing required libraries
from multiapp import MultiApp
import streamlit as st
import pandas as pd

#Reading the required data

def asearch():
    st.title("Artistic Style Similarity Search Method")

    def get_data():
        return pd.read_csv('Artistic.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    c = st.selectbox('Select the Input Method', ('Upload your Image', 'Select image from existing'))
    if c == 'Upload your Image':
        uploaded_file = st.file_uploader("Choose an image from your PC", type="jpeg")
        if uploaded_file is not None:
            st.image(pic, width=None)
            z = st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)
            if st.button('Submit'):
                st.subheader("Similar Products")
                for index, row in df.iterrows():
                    if row['0'] == pic:
                        while n < z + 1:
                            st.image(row[n], width=100, caption=row[n])
                            n += 1
    if c == 'Select image from existing':
        st.subheader("Choose an image from the below menu: ")
        pic = st.selectbox('Choices : ', images)
        st.image(pic, width=None)
        st.subheader('Similar images to be shown?')
        z = st.slider('Similar images to be shown?', 1, 10, 1)
        st.subheader("Similar Products")
        for index, row in df.iterrows():
            if row['0'] == pic:
                while n < z + 1:
                    st.image(row[n], width=100, caption=row[n])
                    n += 1

def fbfa():
    st.title("Facebook FAISS")

    def get_data():
        return pd.read_csv('Faiss.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    c = st.selectbox('Select the Input Method', ('Upload your Image', 'Select image from existing'))
    if c == 'Upload your Image':
        uploaded_file = st.file_uploader("Choose an image from your PC", type="jpeg")
        if uploaded_file is not None:
            st.image(pic, width=None)
            z = st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)
            if st.button('Submit'):
                st.subheader("Similar Products")
                for index, row in df.iterrows():
                    if row['0'] == pic:
                        while n < z + 1:
                            st.image(row[n], width=100, caption=row[n])
                            n += 1
    if c == 'Select image from existing':
        st.subheader("Choose an image from the below menu: ")
        pic = st.selectbox('Choices : ', images)
        st.image(pic, width=None)
        st.subheader('Similar images to be shown?')
        z = st.slider('Similar images to be shown?', 1, 10, 1)
        st.subheader("Similar Products")
        for index, row in df.iterrows():
            if row['0'] == pic:
                while n < z + 1:
                    st.image(row[n], width=100, caption=row[n])
                    n += 1

app = MultiApp()
app.add_app("Artistic Style Similarity Search", asearch)
app.add_app("Facebook FAISS", fbfa)
app.run()