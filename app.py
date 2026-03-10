import streamlit as st
from floor1 import floor_data as floor1
from floor2 import floor_data as floor2
from floor3 import floor_data as floor3
from floor4 import floor_data as floor4
import os

BASE_DIR = os.path.dirname(__file__)

st.title("🏫 Навігатор школи")
st.image("images/school.jpg", caption="Наша школа", width=800)
st.divider()

floors = {
    "1 поверх": floor1,
    "2 поверх": floor2,
    "3 поверх": floor3,
    "4 поверх": floor4
}

tab1, tab2 = st.tabs(["🔎 Пошук", "🗺 Поверхи"])


with tab1:
    
    st.header("Пошук кабінету")

    room_number = st.text_input("Введіть номер кабінету:")

    if room_number != "":
        found = False

        # Перебираємо всі поверхи
        for floor_name in floors:

            # Отримуємо кабінети цього поверху
            rooms = floors[floor_name]

            # Перевіряємо, чи є такий кабінет
            if room_number in rooms:

                room = rooms[room_number]

                st.success("Кабінет знайдено!")
                st.write("Поверх:", floor_name)
                st.write("Назва:", room["name"])
                st.write("Вчитель:", room["teacher"])
                st.write("Опис:", room["description"])

                if room["photo"] != "":
                    st.image(room["photo"], width=300)

                found = True

        if found == False:
            st.error("Такого кабінету немає.")

    
    


with tab2:
    st.header("Поверхи школи")

    floor_tabs = st.tabs(list(floors.keys()))

    for i, floor_name in enumerate(floors.keys()):
        with floor_tabs[i]:

            st.subheader(floor_name)

            # Показуємо план поверху
            st.image(f"images/{floor_name}.jpg",
                     caption=f"План {floor_name}",
                     width="stretch")

            st.write("Оберіть кабінет на плані:")

            rooms = floors[floor_name]

            if len(rooms) > 0:

                # Робимо кнопки в кілька колонок (виглядає акуратніше)
                cols = st.columns(4)

                room_numbers = list(rooms.keys())

                for index in range(len(room_numbers)):
                    room_number = room_numbers[index]
                    room_info = rooms[room_number]

                    col = cols[index % 4]

                    with col:
                        if st.button(room_number):
                            st.subheader(f"{room_number} — {room_info['name']}")
                            st.write("👩‍🏫 Вчитель:", room_info["teacher"])
                            st.write("📝 Опис:", room_info["description"])
                            image_path = os.path.join(BASE_DIR, room_info["photo"])


                            if room_info["photo"] != "":
                                st.image(image_path, width=300)
                               # with st.expander("🔍 Переглянути фото повністю"):
                                #    st.image(image_path,width="stretch")

            else:
                st.info("Інформація ще не додана.")
