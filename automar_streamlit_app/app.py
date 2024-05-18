---
permalink: https://mercyi4ihrj.github.io/automar_streamlit_app/
---
import streamlit as st
import pandas as pd

st.image('imgur/autoteg.psd')

page = st.sidebar.radio('Выбор.', ["Покраска", "очистка от ржавчины"])
if page == "Покраска":
    st.title('Покраска')
    st.header('В этой статье мы разберём все о  :blue[покраске авто] .')
    painting_order = st.radio(
        "Для начала выберите этап покраски :", [" 1 : Мойка авто.", " 2 : Удаление ржавчины.", " 3 : Шпаклевание", " 4 : Грунтование", " 5 : Покраска", " 6 : Полировка" ]
    )
    if painting_order == " 1 : Мойка авто." :
        st.title(':violet[Мойка авто]')
        st.markdown("Перед покраской авто нужно тщательно очистить его кузов.Для лучшей оценки :blue[ЛКП (Лако Красочного Покрытия)] необходимо удалить все пятна.Для очистки кузов обрабатывается стандартными моющими средствами.Затем требуется удалить битумные пятна, если таковые имеются, остатки насекомых и другие сложные загрязнения.Для этого испульзуются спициальные составы.")
        st.image('imgur/Bitumavto.jpg', caption = 'Битумные пятна')

    elif painting_order == " 2 : Удаление ржавчины." :
        st.title(':violet[Удаление ржавчины]')

    elif painting_order == " 3 : Шпаклевание" :
        st.title(':violet[Шпаклевание]')

    elif painting_order == " 4 : Грунтование" :
        st.title(':violet[Грунтование]')

    elif painting_order == " 5 : Покраска" :
        st.title(':violet[Покраска]')

    elif painting_order == " 6 : Полировка" :
        st.title(':violet[Полировка]')
