# Limnology Teaching Assistant System

---

## ** Overview**

The **Limnology Teaching Assistant System** is a **Python-based automation tool** designed to support **teaching and research** in **freshwater ecosystem studies**. This system streamlines the **lab and field components** of limnology courses, including **water sampling techniques, invertebrate collection, taxonomic identification, and chemical analysis**. It facilitates **hands-on learning** by managing **field trips on the UVM research vessel *Marcelle Melosira***, standard sampling gear (e.g., Niskin bottles, Secchi discs, plankton nets, Van Dorn samplers), and student support activities like **office hours and grading**.

---

## ** Features**

---

### **Course Management**

- **Course Creation**: Set up **limnology courses** with semesters, instructors, and student rosters.
- **Student Tracking**: Manage **student records**, including **attendance, grades, and participation** in lab and field activities.
- **Roster Management**: Add and track students with **contact information and academic progress**.

---

### **Lab Sessions**

- **Session Scheduling**: Plan **lab sessions** with **topics, locations, and activities** (e.g., water sampling techniques, chemical analysis).
- **Activity Management**: Add and track **lab activities** such as:
  - Instructions on using **Niskin bottles, Secchi discs, plankton nets, and Van Dorn samplers**.
  - **Chemical analysis** of water samples (phosphorus, nitrogen, pH, conductivity).
- **Status Tracking**: Monitor lab session statuses (Scheduled, Conducted, Cancelled).

---

### **Field Trips**

- **Trip Scheduling**: Organize **field trips** to freshwater ecosystems like **Lake Champlain** and other inland lakes in Vermont.
- **Vessel Management**: Track the use of the **UVM research vessel *Marcelle Melosira*** for field excursions.
- **Gear Usage**: Log the use of **standard limnological sampling gear**, including:
  - **Niskin bottles** (water sampling at specific depths).
  - **Secchi discs** (water transparency measurements).
  - **Plankton nets** (zooplankton collection).
  - **Van Dorn samplers** (vertical water column sampling).
- **Status Tracking**: Monitor field trip statuses (Scheduled, Conducted, Cancelled).

---

### **Sampling Events**

- **Event Recording**: Document **sampling events** during field trips, including:
  - **Location** (e.g., Station A, Station B).
  - **Gear used** (e.g., Niskin bottle, plankton net).
  - **Samples collected** (water, zooplankton, benthic invertebrates).
- **Sample Types**: Track **water samples** (depth, volume) and **biological samples** (duration, method).

---

### **Invertebrate Sampling and Identification**

- **Sample Collection**: Collect and preserve **invertebrate samples** from freshwater ecosystems.
- **Taxonomic Identification**: Assist students in identifying **aquatic invertebrates and zooplankton** using:
  - **Microscopy** (dissecting and compound microscopes).
  - **Taxonomic keys** for classifying freshwater organisms (e.g., *Daphnia pulex*, *Cyclops*, bloodworms, caddisfly larvae).
- **Organism Database**: Predefined database of **common freshwater organisms** with:
  - **Scientific and common names**.
  - **Taxonomic groups** (e.g., Zooplankton, Benthic Invertebrates).
  - **Identification tips** for students.

---

### **Water Sampling and Chemical Analysis**

- **Water Sample Collection**: Collect **water samples** for chemical analysis using standard limnological tools.
- **Chemical Analysis**: Perform **tests for key water quality parameters**, including:
  - **Phosphorus** (µg/L, Spectrophotometer).
  - **Nitrogen** (mg/L, Colorimetry).
  - **pH** (pH Meter).
  - **Conductivity** (µS/cm, Conductivity Meter).
  - **Dissolved Oxygen** (mg/L, DO Meter).
- **Parameter Tracking**: Monitor **water quality parameters** with predefined **normal ranges** for freshwater ecosystems.

---

### **Student Support**

- **Attendance Tracking**: Record **student attendance** for lab sessions and field trips.
- **Grade Management**: Track **student grades** for assignments, lab reports, and participation.
- **Office Hours**: Schedule and document **office hours** for academic support, including:
  - **Topics discussed** (e.g., water sampling techniques, invertebrate ID).
  - **Notes** on student inquiries and discussions.
- **Academic Support**: Reinforce **course content** and provide guidance on **field/lab techniques**.

---

### **Audit Logging**

- **Activity Tracking**: Automatically log all actions (e.g., lab sessions, sampling events, chemical analyses) for **traceability and compliance**.
- **Comprehensive Logs**: Retrieve logs for **auditing, reporting, and debugging**.

---

### **Reporting**

- **Course Reports**: Generate **detailed reports** for courses, including:
  - **Students** (attendance, grades).
  - **Lab sessions** (topics, activities, status).
  - **Field trips** (locations, gear used, sampling events).
  - **Invertebrate samples** (organisms identified, preservation methods).
  - **Water samples and chemical analyses** (parameters tested, results).
- **Student Reports**: Summarize **attendance, grades, office hours visits, and invertebrate identifications** for each student.
- **Field Trip Reports**: Document **sampling events, invertebrate samples, water samples, and chemical analyses** for each field trip.

---

## ** Installation**

### **Prerequisites**

- **Python 3.8+**
- **Dependencies**: None (uses Python’s built-in libraries)

### **Setup**

1. **Clone the repository**:
  ```bash
   git clone https://github.com/Bukkysash/limnology-system
   cd limnology-system
  ```
2. **Run the system**:
  ```bash
   python limnology_ta_system.py
  ```

---

## **🛠️ Usage**

---

### **1. Initialize the System**

```python
ta_system = LimnologyTASystem()
```

---

### **2. Course Management**

```python
# Create a limnology course
course_id = ta_system.create_course(
    "Limnology (NR 145)",
    "Fall 2023",
    "Dr. Johnson",
    ["Alice", "Bob", "Charlie"]
)

# Add a student (if not already added via course creation)
student_id = ta_system.add_student("David", "david@uvm.edu")
```

---

### **3. Lab Sessions**

```python
# Schedule a lab session
lab_id = ta_system.schedule_lab_session(
    course_id,
    "2023-09-10",
    "Water Sampling Techniques",
    "UVM Lab",
    ["Niskin Bottle Demo", "Secchi Disc Usage"]
)

# Add an activity to the lab session
ta_system.add_lab_activity(lab_id, "pH and Conductivity Testing")

# Mark the lab session as conducted
ta_system.conduct_lab_session(lab_id)
```

---

### **4. Field Trips**

```python
# Schedule a field trip
trip_id = ta_system.schedule_field_trip(
    course_id,
    "2023-09-15",
    "Lake Champlain",
    "Marcelle Melosira"
)

# Record the use of sampling gear
ta_system.use_sampling_gear(trip_id, "Niskin Bottle")
ta_system.use_sampling_gear(trip_id, "Plankton Net")
ta_system.use_sampling_gear(trip_id, "Secchi Disc")

# Mark the field trip as conducted
ta_system.conduct_field_trip(trip_id)
```

---

### **5. Sampling Events**

```python
# Record a sampling event
event_id_1 = ta_system.record_sampling_event(
    trip_id,
    "Station A",
    "Niskin Bottle",
    [{"type": "Water", "depth": "5m", "volume": "1L"}]
)

event_id_2 = ta_system.record_sampling_event(
    trip_id,
    "Station B",
    "Plankton Net",
    [{"type": "Zooplankton", "depth": "0-1m", "duration": "5 min"}]
)
```

---

### **6. Invertebrate Sampling and Identification**

```python
# Collect invertebrate samples
sample_id_1 = ta_system.collect_invertebrate_sample(
    event_id_1,
    "Station A",
    ["Daphnia pulex", "Cyclops"],
    "Ethanol"
)

sample_id_2 = ta_system.collect_invertebrate_sample(
    event_id_2,
    "Station B",
    ["Water Flea", "Rotifer"]
)

# Assist students with identifying organisms
ta_system.identify_organisms(
    sample_id_1,
    "STU1",
    [
        {"common_name": "Water Flea", "scientific_name": "Daphnia pulex", "taxa_group": "Zooplankton", "confidence": "High"},
        {"common_name": "Cyclops", "scientific_name": "Cyclops sp.", "taxa_group": "Zooplankton", "confidence": "Medium"}
    ]
)
```

---

### **7. Water Sampling and Chemical Analysis**

```python
# Collect water samples
water_sample_id = ta_system.collect_water_sample(
    event_id_1,
    "Station A",
    ["Phosphorus", "Nitrogen", "pH"]
)

# Perform chemical analysis
ta_system.perform_chemical_analysis(water_sample_id, "Phosphorus", 45.2, "Spectrophotometer")
ta_system.perform_chemical_analysis(water_sample_id, "Nitrogen", 2.1, "Colorimetry")
ta_system.perform_chemical_analysis(water_sample_id, "pH", 7.8, "pH Meter")
```

---

### **8. Student Support**

```python
# Record student attendance
ta_system.record_attendance(lab_id, "STU1", "Present")
ta_system.record_attendance(lab_id, "STU2", "Present")

# Record grades
ta_system.record_grade("STU1", "Lab Report 1", 92.5)
ta_system.record_grade("STU2", "Lab Report 1", 88.0)

# Schedule office hours
office_hour_id = ta_system.schedule_office_hours(
    "2023-09-20",
    ["STU1", "STU3"],
    ["Water Sampling Questions", "Invertebrate ID Help"]
)

# Add notes to office hours
ta_system.add_office_hours_notes(
    office_hour_id,
    "Discussed Niskin bottle technique with STU1. Reviewed zooplankton ID with STU3."
)
```

---

### **9. Generate Reports**

```python
# Generate a course report
course_report = ta_system.generate_course_report(course_id)

# Generate a student report
student_report = ta_system.generate_student_report("STU1")

# Generate a field trip report
trip_report = ta_system.generate_field_trip_report(trip_id)
```

---

## ** Repository Structure**

```
.
├── limnology-system.py  # Main system code
├── README.md               # Project documentation
└── requirements.txt        # Dependencies (if any)
```

---

## ** Technical Details**

---

### **Architecture**

- **Class-Based Design**: The `LimnologyTASystem` class encapsulates all functionalities.
- **Data Storage**: Uses **dictionaries and lists** for in-memory storage (suitable for small-to-medium datasets).
- **Unique Identifiers**: Sequential IDs ensure **unique tracking** of courses, sessions, trips, samples, and students.
- **Audit Logging**: Tracks all actions for **compliance, traceability, and debugging**.

---

### **Extensibility**

Future enhancements could include:

- **Database Integration**: Use `sqlite3` or `PostgreSQL` for persistent storage of course data, sampling events, and student records.
- **Data Visualization**: Integrate `matplotlib`, `seaborn`, or `plotly` for generating **plots of water quality trends, zooplankton abundance, and chemical analysis results**.
- **Web Interface**: Deploy with **Flask/Django** for a user-friendly dashboard to manage courses, lab sessions, and field trips.
- **R Integration**: Add support for **R scripts** to perform advanced statistical analyses (e.g., ANOVA, PCA) on limnological data.
- **Equipment API Integration**: Connect with **laboratory equipment APIs** (e.g., YSI sondes, spectrophotometers) for real-time data collection.
- **Collaboration Tools**: Integrate with **Google Classroom or Canvas** for assignment management and grading.

---

## ** Example Output**

Running the example usage in `__main__` produces:

```
=== Course Management ===
Course 'Limnology (NR 145)' created with ID: COURSE1
Student 'David' added with ID: STU4

=== Lab Sessions ===
Lab Session 'Water Sampling Techniques' scheduled with ID: LAB1
Activity 'pH and Conductivity Testing' added to Lab Session LAB1
Lab Session LAB1 marked as conducted.

=== Field Trips ===
Field Trip to Lake Champlain scheduled with ID: TRIP1
Sampling gear 'Niskin Bottle' used during Field Trip TRIP1
Sampling gear 'Plankton Net' used during Field Trip TRIP1
Sampling gear 'Secchi Disc' used during Field Trip TRIP1
Field Trip TRIP1 marked as conducted.

=== Sampling Events ===
Sampling Event recorded with ID: EVENT1
Sampling Event recorded with ID: EVENT2

=== Invertebrate Sampling ===
Invertebrate Sample collected with ID: INV1
Invertebrate Sample collected with ID: INV2
Organisms identified in Sample INV1 by Student STU1

=== Water Sampling and Chemical Analysis ===
Water Sample collected with ID: WATER1
Chemical Analysis performed with ID: CHEM1. Phosphorus: 45.2 µg/L
Chemical Analysis performed with ID: CHEM2. Nitrogen: 2.1 mg/L
Chemical Analysis performed with ID: CHEM3. pH: 7.8

=== Student Support ===
Attendance recorded for Student STU1 in Session LAB1: Present
Attendance recorded for Student STU2 in Session LAB1: Present
Grade recorded for Student STU1. Lab Report 1: 92.5%
Grade recorded for Student STU2. Lab Report 1: 88.0%
Office Hours scheduled with ID: OH1
Notes added to Office Hours OH1

=== Course Report ===
course_id: COURSE1
name: Limnology (NR 145)
semester: Fall 2023
instructor: Dr. Johnson
students: [{'student_id': 'STU1', 'name': 'Alice', ...}, ...]
lab_sessions: [{'session_id': 'LAB1', 'topic': 'Water Sampling Techniques', ...}]
field_trips: [{'trip_id': 'TRIP1', 'location': 'Lake Champlain', ...}]
invertebrate_samples: [{'sample_id': 'INV1', 'location': 'Station A', ...}, ...]
water_samples: [{'sample_id': 'WATER1', 'location': 'Station A', ...}]
chemical_analyses: [{'analysis_id': 'CHEM1', 'parameter': 'Phosphorus', ...}, ...]

=== Student Report for Alice ===
student_id: STU1
name: Alice
email: alice@uvm.edu
attendance: {'LAB1': 'Present'}
grades: {'Lab Report 1': 92.5}
office_hours_visited: [{'hour_id': 'OH1', 'date': '2023-09-20', ...}]
invertebrate_identifications: [{'sample_id': 'INV1', 'organisms': [...]}]

=== Field Trip Report for Lake Champlain ===
trip_id: TRIP1
course_id: COURSE1
date: 2023-09-15
location: Lake Champlain
vessel: Marcelle Melosira
gear_used: ['Niskin Bottle', 'Plankton Net', 'Secchi Disc']
sampling_events: [{'event_id': 'EVENT1', 'location': 'Station A', ...}, ...]
invertebrate_samples: [{'sample_id': 'INV1', 'location': 'Station A', ...}, ...]
water_samples: [{'sample_id': 'WATER1', 'location': 'Station A', ...}]
chemical_analyses: [{'analysis_id': 'CHEM1', 'parameter': 'Phosphorus', ...}, ...]
```

---

## ** Contributing**

Contributions are welcome! To contribute:

1. **Fork the repository** and create a feature branch.
2. **Add improvements**:
  - Database integration (e.g., SQLite).
  - Data visualization tools (e.g., `matplotlib`, `seaborn`).
  - Advanced statistical analyses (e.g., using `scipy` or `pandas`).
3. **Submit a pull request** with a clear description of changes.

---

## ** License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ** Acknowledgments**

- Designed to support **hands-on learning** in **freshwater ecosystem studies**.
- Built to streamline **lab/field instruction, sampling, taxonomic identification, and chemical analysis** for students and teaching assistants.
