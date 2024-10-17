import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Title of the app
st.title("Feeding and Vaccination Tracker")

# Create an empty DataFrame to store feeding and vaccination records
if 'records' not in st.session_state:
    st.session_state.records = pd.DataFrame(columns=["Type", "Date", "Next Time"])

# Initialize session state for time inputs
if 'feeding_time' not in st.session_state:
    st.session_state.feeding_time = datetime.now().time()
if 'vaccination_time' not in st.session_state:
    st.session_state.vaccination_time = datetime.now().time()

# Function to calculate the next feeding time
def calculate_next_feeding(current_time, interval_hours):
    return current_time + timedelta(hours=interval_hours)

st.divider()
# Input section for feeding details
st.header("Feeding Schedule")
feeding_time_input = st.time_input("Enter feeding time (HH:MM)", value=st.session_state.feeding_time)
feeding_interval = st.number_input("Enter feeding interval (in hours)", min_value=1, max_value=12, step=1)

if st.button("Add Feeding"):
    current_time = datetime.combine(datetime.today(), feeding_time_input)
    next_time = calculate_next_feeding(current_time, feeding_interval)
    new_record = pd.DataFrame({"Type": ["Feeding"], "Date": [current_time], "Next Time": [next_time]})
    st.session_state.records = pd.concat([st.session_state.records, new_record], ignore_index=True)
    # Update the feeding time in session state
    st.session_state.feeding_time = feeding_time_input

    # Show the next feeding time to the user
    st.success(f"The next feeding is scheduled at: {next_time.strftime('%H:%M')}")

st.divider()
# Input section for vaccination details
st.header("Vaccination Schedule")
vaccination_date_input = st.date_input("Enter vaccination date", value=datetime.today())
vaccination_time_input = st.time_input("Enter vaccination time (HH:MM)", value=st.session_state.vaccination_time)

if st.button("Add Vaccination"):
    vaccination_time = datetime.combine(vaccination_date_input, vaccination_time_input)
    new_record = pd.DataFrame({"Type": ["Vaccination"], "Date": [vaccination_time], "Next Time": ["N/A"]})
    st.session_state.records = pd.concat([st.session_state.records, new_record], ignore_index=True)
    # Update the vaccination time in session state
    st.session_state.vaccination_time = vaccination_time_input

st.divider()
# Display the records table
st.header("Records")
st.write(st.session_state.records)

# Provide reminders
if st.session_state.records.shape[0] > 0:
    st.header("Reminders")
    now = datetime.now()
    for index, row in st.session_state.records.iterrows():
        if row["Type"] == "Feeding":
            next_feed_time = row["Next Time"]
            st.write(f"Next feeding is scheduled at: {next_feed_time.strftime('%Y-%m-%d %H:%M')}")
            # Check if the feeding time is now or in the next few minutes
            if now >= next_feed_time - timedelta(minutes=5) and now < next_feed_time:
                st.warning(f"Reminder: It's almost time to feed! Next feeding is at: {next_feed_time.strftime('%H:%M')}.")
        elif row["Type"] == "Vaccination":
            st.write(f"Vaccination scheduled at: {row['Date'].strftime('%Y-%m-%d %H:%M')}")
            # Check if the vaccination time is now or in the next few minutes
            if now >= row["Date"] - timedelta(minutes=5) and now < row["Date"]:
                st.warning(f"Reminder: It's almost time for vaccination at: {row['Date'].strftime('%H:%M')}.")

st.divider()
# Option to download the records as a CSV file
st.header("Click to Download Records")
csv = st.session_state.records.to_csv(index=False).encode('utf-8')
st.download_button("Download Records as CSV", csv, "feeding_vaccination_records.csv", "text/csv", key='download-csv')

st.divider()
# Calendar visualization placeholder (you would implement this separately)
st.header("Calendar Visualization (to be implemented)")
st.write("This section would show a calendar with feeding and vaccination times marked.")
