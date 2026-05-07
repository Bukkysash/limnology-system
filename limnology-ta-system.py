import datetime
from typing import Dict, List, Optional, Tuple, Union
import uuid
import random
from dataclasses import dataclass

@dataclass
class SamplingGear:
    """Class to represent sampling gear with specifications."""
    name: str
    type: str
    description: str
    usage_instructions: str

@dataclass
class AquaticOrganism:
    """Class to represent aquatic organisms with taxonomic information."""
    common_name: str
    scientific_name: str
    taxa_group: str  # e.g., Zooplankton, Benthic Invertebrates
    identification_tips: str

@dataclass
class WaterQualityParameter:
    """Class to represent water quality parameters and testing methods."""
    name: str
    unit: str
    method: str
    normal_range: Tuple[float, float]

class LimnologyTASystem:
    def __init__(self):
        # Courses: {course_id: {"name": str, "semester": str, "instructor": str, "students": List[str]}}
        self.courses: Dict[str, Dict] = {}

        # Lab Sessions: {session_id: {"course_id": str, "date": str, "topic": str, "location": str, "activities": List[str]}}
        self.lab_sessions: Dict[str, Dict] = {}

        # Field Trips: {trip_id: {"course_id": str, "date": str, "location": str, "vessel": str, "gear_used": List[str]}}
        self.field_trips: Dict[str, Dict] = {}

        # Sampling Events: {event_id: {"trip_id": str, "date": str, "location": str, "gear": str, "samples": List[Dict]}}
        self.sampling_events: Dict[str, Dict] = {}

        # Invertebrate Samples: {sample_id: {"event_id": str, "location": str, "date": str, "organisms": List[Dict], "preservation": str}}
        self.invertebrate_samples: Dict[str, Dict] = {}

        # Water Samples: {sample_id: {"event_id": str, "location": str, "date": str, "parameters": List[WaterQualityParameter]}}
        self.water_samples: Dict[str, Dict] = {}

        # Chemical Analysis: {analysis_id: {"sample_id": str, "parameter": str, "value": float, "method": str, "date": str}}
        self.chemical_analyses: Dict[str, Dict] = {}

        # Taxonomic Keys: {key_id: {"name": str, "taxa_group": str, "description": str}}
        self.taxonomic_keys: Dict[str, Dict] = {}

        # Student Records: {student_id: {"name": str, "email": str, "attendance": Dict, "grades": Dict}}
        self.students: Dict[str, Dict] = {}

        # Office Hours: {hour_id: {"date": str, "students": List[str], "topics": List[str], "notes": str}}
        self.office_hours: Dict[str, Dict] = {}

        # Audit Logs: List[Dict]
        self.audit_logs: List[Dict] = {}

        # Predefined Sampling Gear
        self.sampling_gear = [
            SamplingGear("Niskin Bottle", "Water Sampler", "For collecting water at specific depths", "Lower to desired depth, trigger to close"),
            SamplingGear("Secchi Disc", "Transparency", "Measures water clarity", "Lower until disc disappears, record depth"),
            SamplingGear("Plankton Net", "Plankton Sampler", "For collecting zooplankton", "Tow horizontally at slow speed"),
            SamplingGear("Van Dorn Sampler", "Water Sampler", "For vertical water column sampling", "Lower to depth, trigger to close at both ends"),
            SamplingGear("Ekman Dredge", "Benthic Sampler", "For collecting benthic invertebrates", "Lower to bottom, trigger to close")
        ]

        # Predefined Aquatic Organisms
        self.aquatic_organisms = [
            AquaticOrganism("Water Flea", "Daphnia pulex", "Zooplankton", "Look for transparent body and large antennae"),
            AquaticOrganism("Cyclops", "Cyclops sp.", "Zooplankton", "Small, one-eyed copepods"),
            AquaticOrganism("Bloodworm", "Chironomus sp.", "Benthic Invertebrates", "Red larvae, segmented body"),
            AquaticOrganism("Caddisfly Larva", "Hydropsyche sp.", "Benthic Invertebrates", "Case-building larvae, silken tubes"),
            AquaticOrganism("Rotifer", "Brachionus sp.", "Zooplankton", "Wheel-like ciliated organisms")
        ]

        # Predefined Water Quality Parameters
        self.water_quality_parameters = [
            WaterQualityParameter("Phosphorus", "µg/L", "Spectrophotometer", (0, 100)),
            WaterQualityParameter("Nitrogen", "mg/L", "Colorimetry", (0, 10)),
            WaterQualityParameter("pH", "", "pH Meter", (6.5, 8.5)),
            WaterQualityParameter("Conductivity", "µS/cm", "Conductivity Meter", (0, 1000)),
            WaterQualityParameter("Dissolved Oxygen", "mg/L", "DO Meter", (5, 15))
        ]

        # Predefined Taxonomic Keys
        self.taxonomic_keys = {
            "ZOOPLANKTON": {
                "name": "Freshwater Zooplankton Key",
                "taxa_group": "Zooplankton",
                "description": "Key for identifying common freshwater zooplankton"
            },
            "BENTHIC": {
                "name": "Benthic Invertebrates Key",
                "taxa_group": "Benthic Invertebrates",
                "description": "Key for identifying benthic macroinvertebrates"
            }
        }

        # Next IDs
        self.next_course_id = 1
        self.next_session_id = 1
        self.next_trip_id = 1
        self.next_event_id = 1
        self.next_sample_id = 1
        self.next_analysis_id = 1
        self.next_student_id = 1
        self.next_hour_id = 1

    # --- Course Management ---
    def create_course(self, name: str, semester: str, instructor: str, students: List[str]) -> str:
        """Create a new limnology course."""
        course_id = f"COURSE{self.next_course_id}"
        self.next_course_id += 1
        self.courses[course_id] = {
            "name": name,
            "semester": semester,
            "instructor": instructor,
            "students": students,
            "status": "Active"
        }
        # Add students to the system
        for student in students:
            self.add_student(student)
        self._log_activity("course_created", {
            "course_id": course_id,
            "name": name,
            "semester": semester
        })
        return f"Course '{name}' created with ID: {course_id}"

    def add_student(self, name: str, email: Optional[str] = None) -> str:
        """Add a student to the system."""
        student_id = f"STU{self.next_student_id}"
        self.next_student_id += 1
        self.students[student_id] = {
            "name": name,
            "email": email if email else f"{name.lower().replace(' ', '.')}@uvm.edu",
            "attendance": {},
            "grades": {}
        }
        self._log_activity("student_added", {"student_id": student_id, "name": name})
        return f"Student '{name}' added with ID: {student_id}"

    # --- Lab Sessions ---
    def schedule_lab_session(self, course_id: str, date: str, topic: str, location: str, activities: List[str]) -> str:
        """Schedule a lab session for a course."""
        if course_id in self.courses:
            session_id = f"LAB{self.next_session_id}"
            self.next_session_id += 1
            self.lab_sessions[session_id] = {
                "course_id": course_id,
                "date": date,
                "topic": topic,
                "location": location,
                "activities": activities,
                "status": "Scheduled"
            }
            self._log_activity("lab_session_scheduled", {
                "session_id": session_id,
                "course_id": course_id,
                "topic": topic
            })
            return f"Lab Session '{topic}' scheduled with ID: {session_id}"
        return f"Course ID {course_id} not found."

    def conduct_lab_session(self, session_id: str) -> str:
        """Mark a lab session as conducted."""
        if session_id in self.lab_sessions:
            self.lab_sessions[session_id]["status"] = "Conducted"
            self._log_activity("lab_session_conducted", {"session_id": session_id})
            return f"Lab Session {session_id} marked as conducted."
        return f"Lab Session ID {session_id} not found."

    def add_lab_activity(self, session_id: str, activity: str) -> str:
        """Add an activity to a lab session."""
        if session_id in self.lab_sessions:
            self.lab_sessions[session_id]["activities"].append(activity)
            self._log_activity("lab_activity_added", {
                "session_id": session_id,
                "activity": activity
            })
            return f"Activity '{activity}' added to Lab Session {session_id}"
        return f"Lab Session ID {session_id} not found."

    # --- Field Trips ---
    def schedule_field_trip(self, course_id: str, date: str, location: str, vessel: str = "Marcelle Melosira") -> str:
        """Schedule a field trip for a course."""
        if course_id in self.courses:
            trip_id = f"TRIP{self.next_trip_id}"
            self.next_trip_id += 1
            self.field_trips[trip_id] = {
                "course_id": course_id,
                "date": date,
                "location": location,
                "vessel": vessel,
                "gear_used": [],
                "status": "Scheduled"
            }
            self._log_activity("field_trip_scheduled", {
                "trip_id": trip_id,
                "course_id": course_id,
                "location": location
            })
            return f"Field Trip to {location} scheduled with ID: {trip_id}"
        return f"Course ID {course_id} not found."

    def conduct_field_trip(self, trip_id: str) -> str:
        """Mark a field trip as conducted."""
        if trip_id in self.field_trips:
            self.field_trips[trip_id]["status"] = "Conducted"
            self._log_activity("field_trip_conducted", {"trip_id": trip_id})
            return f"Field Trip {trip_id} marked as conducted."
        return f"Field Trip ID {trip_id} not found."

    def use_sampling_gear(self, trip_id: str, gear_name: str) -> str:
        """Record the use of sampling gear during a field trip."""
        if trip_id in self.field_trips:
            gear = next((g for g in self.sampling_gear if g.name == gear_name), None)
            if gear:
                self.field_trips[trip_id]["gear_used"].append(gear_name)
                self._log_activity("gear_used", {
                    "trip_id": trip_id,
                    "gear": gear_name
                })
                return f"Sampling gear '{gear_name}' used during Field Trip {trip_id}"
            return f"Sampling gear '{gear_name}' not found."
        return f"Field Trip ID {trip_id} not found."

    # --- Sampling Events ---
    def record_sampling_event(self, trip_id: str, location: str, gear: str, samples: List[Dict]) -> str:
        """Record a sampling event during a field trip."""
        if trip_id in self.field_trips:
            event_id = f"EVENT{self.next_event_id}"
            self.next_event_id += 1
            self.sampling_events[event_id] = {
                "trip_id": trip_id,
                "date": self.field_trips[trip_id]["date"],
                "location": location,
                "gear": gear,
                "samples": samples
            }
            self._log_activity("sampling_event_recorded", {
                "event_id": event_id,
                "trip_id": trip_id,
                "location": location
            })
            return f"Sampling Event recorded with ID: {event_id}"
        return f"Field Trip ID {trip_id} not found."

    # --- Invertebrate Sampling and Identification ---
    def collect_invertebrate_sample(self, event_id: str, location: str, organisms: List[str], preservation: str = "Ethanol") -> str:
        """Collect and preserve invertebrate samples."""
        if event_id in self.sampling_events:
            sample_id = f"INV{self.next_sample_id}"
            self.next_sample_id += 1
            organism_details = []
            for org_name in organisms:
                org = next((o for o in self.aquatic_organisms if o.common_name == org_name or o.scientific_name == org_name), None)
                if org:
                    organism_details.append({
                        "common_name": org.common_name,
                        "scientific_name": org.scientific_name,
                        "taxa_group": org.taxa_group,
                        "identification_tips": org.identification_tips
                    })

            self.invertebrate_samples[sample_id] = {
                "event_id": event_id,
                "location": location,
                "date": self.sampling_events[event_id]["date"],
                "organisms": organism_details,
                "preservation": preservation
            }
            self._log_activity("invertebrate_sample_collected", {
                "sample_id": sample_id,
                "event_id": event_id,
                "organisms": organisms
            })
            return f"Invertebrate Sample collected with ID: {sample_id}"
        return f"Sampling Event ID {event_id} not found."

    def identify_organisms(self, sample_id: str, student_id: str, identifications: List[Dict]) -> str:
        """Assist students with identifying aquatic organisms using taxonomic keys."""
        if sample_id in self.invertebrate_samples and student_id in self.students:
            # Update the sample with student identifications
            for id_record in identifications:
                self.invertebrate_samples[sample_id]["organisms"].append({
                    "identified_by": student_id,
                    "common_name": id_record.get("common_name"),
                    "scientific_name": id_record.get("scientific_name"),
                    "taxa_group": id_record.get("taxa_group"),
                    "confidence": id_record.get("confidence", "High")
                })
            self._log_activity("organisms_identified", {
                "sample_id": sample_id,
                "student_id": student_id,
                "identifications": identifications
            })
            return f"Organisms identified in Sample {sample_id} by Student {student_id}"
        return f"Sample ID {sample_id} or Student ID {student_id} not found."

    # --- Water Sampling and Chemical Analysis ---
    def collect_water_sample(self, event_id: str, location: str, parameters: List[str]) -> str:
        """Collect water samples for chemical analysis."""
        if event_id in self.sampling_events:
            sample_id = f"WATER{self.next_sample_id}"
            self.next_sample_id += 1
            parameter_objects = []
            for param_name in parameters:
                param = next((p for p in self.water_quality_parameters if p.name == param_name), None)
                if param:
                    parameter_objects.append(param)

            self.water_samples[sample_id] = {
                "event_id": event_id,
                "location": location,
                "date": self.sampling_events[event_id]["date"],
                "parameters": parameter_objects
            }
            self._log_activity("water_sample_collected", {
                "sample_id": sample_id,
                "event_id": event_id,
                "parameters": parameters
            })
            return f"Water Sample collected with ID: {sample_id}"
        return f"Sampling Event ID {event_id} not found."

    def perform_chemical_analysis(self, sample_id: str, parameter: str, value: float, method: str) -> str:
        """Perform chemical analysis on a water sample."""
        if sample_id in self.water_samples:
            analysis_id = f"CHEM{self.next_analysis_id}"
            self.next_analysis_id += 1
            self.chemical_analyses[analysis_id] = {
                "sample_id": sample_id,
                "parameter": parameter,
                "value": value,
                "method": method,
                "date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
            self._log_activity("chemical_analysis_performed", {
                "analysis_id": analysis_id,
                "sample_id": sample_id,
                "parameter": parameter,
                "value": value
            })
            return f"Chemical Analysis performed with ID: {analysis_id}. {parameter}: {value} {next(p.unit for p in self.water_quality_parameters if p.name == parameter)}"
        return f"Water Sample ID {sample_id} not found."

    # --- Student Support ---
    def record_attendance(self, session_id: str, student_id: str, status: str = "Present") -> str:
        """Record student attendance for a lab session or field trip."""
        if session_id in self.lab_sessions and student_id in self.students:
            self.students[student_id]["attendance"][session_id] = status
            self._log_activity("attendance_recorded", {
                "session_id": session_id,
                "student_id": student_id,
                "status": status
            })
            return f"Attendance recorded for Student {student_id} in Session {session_id}: {status}"
        return f"Session ID {session_id} or Student ID {student_id} not found."

    def record_grade(self, student_id: str, assignment: str, grade: float) -> str:
        """Record a grade for a student assignment."""
        if student_id in self.students:
            self.students[student_id]["grades"][assignment] = grade
            self._log_activity("grade_recorded", {
                "student_id": student_id,
                "assignment": assignment,
                "grade": grade
            })
            return f"Grade recorded for Student {student_id}. {assignment}: {grade}%"
        return f"Student ID {student_id} not found."

    def schedule_office_hours(self, date: str, students: List[str], topics: List[str]) -> str:
        """Schedule office hours for student support."""
        hour_id = f"OH{self.next_hour_id}"
        self.next_hour_id += 1
        self.office_hours[hour_id] = {
            "date": date,
            "students": students,
            "topics": topics,
            "notes": ""
        }
        self._log_activity("office_hours_scheduled", {
            "hour_id": hour_id,
            "date": date,
            "topics": topics
        })
        return f"Office Hours scheduled with ID: {hour_id}"

    def add_office_hours_notes(self, hour_id: str, notes: str) -> str:
        """Add notes to office hours (e.g., student questions, discussions)."""
        if hour_id in self.office_hours:
            self.office_hours[hour_id]["notes"] = notes
            self._log_activity("office_hours_notes_added", {
                "hour_id": hour_id,
                "notes": notes
            })
            return f"Notes added to Office Hours {hour_id}"
        return f"Office Hours ID {hour_id} not found."

    # --- Audit Logging ---
    def _log_activity(self, action: str, details: Dict) -> None:
        """Log an activity to the audit trail."""
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        self.audit_logs.append(log_entry)

    def get_audit_logs(self) -> List[Dict]:
        """Retrieve all audit logs."""
        return self.audit_logs

    # --- Reporting ---
    def generate_course_report(self, course_id: str) -> Dict:
        """Generate a comprehensive report for a course."""
        if course_id in self.courses:
            course = self.courses[course_id]
            report = {
                "course_id": course_id,
                "name": course["name"],
                "semester": course["semester"],
                "instructor": course["instructor"],
                "students": [
                    {
                        "student_id": sid,
                        "name": self.students[sid]["name"],
                        "attendance": self.students[sid]["attendance"],
                        "grades": self.students[sid]["grades"]
                    }
                    for sid in course["students"]
                ],
                "lab_sessions": [
                    ls for ls in self.lab_sessions.values()
                    if ls["course_id"] == course_id
                ],
                "field_trips": [
                    ft for ft in self.field_trips.values()
                    if ft["course_id"] == course_id
                ],
                "invertebrate_samples": [
                    inv for inv in self.invertebrate_samples.values()
                    if inv["event_id"] in [e["event_id"] for e in self.sampling_events.values() if e["trip_id"] in [ft["trip_id"] for ft in self.field_trips.values() if ft["course_id"] == course_id]]
                ],
                "water_samples": [
                    ws for ws in self.water_samples.values()
                    if ws["event_id"] in [e["event_id"] for e in self.sampling_events.values() if e["trip_id"] in [ft["trip_id"] for ft in self.field_trips.values() if ft["course_id"] == course_id]]
                ],
                "chemical_analyses": [
                    ca for ca in self.chemical_analyses.values()
                    if ca["sample_id"] in [ws["sample_id"] for ws in self.water_samples.values() if ws["event_id"] in [e["event_id"] for e in self.sampling_events.values() if e["trip_id"] in [ft["trip_id"] for ft in self.field_trips.values() if ft["course_id"] == course_id]]]
                ]
            }
            return report
        return {"error": "Course ID not found"}

    def generate_student_report(self, student_id: str) -> Dict:
        """Generate a report for a student's performance and activities."""
        if student_id in self.students:
            student = self.students[student_id]
            report = {
                "student_id": student_id,
                "name": student["name"],
                "email": student["email"],
                "attendance": student["attendance"],
                "grades": student["grades"],
                "office_hours_visited": [
                    oh for oh in self.office_hours.values()
                    if student_id in oh["students"]
                ],
                "invertebrate_identifications": [
                    inv for inv in self.invertebrate_samples.values()
                    if any(org.get("identified_by") == student_id for org in inv["organisms"])
                ]
            }
            return report
        return {"error": "Student ID not found"}

    def generate_field_trip_report(self, trip_id: str) -> Dict:
        """Generate a report for a field trip, including sampling events and results."""
        if trip_id in self.field_trips:
            trip = self.field_trips[trip_id]
            report = {
                "trip_id": trip_id,
                "course_id": trip["course_id"],
                "date": trip["date"],
                "location": trip["location"],
                "vessel": trip["vessel"],
                "gear_used": trip["gear_used"],
                "sampling_events": [
                    se for se in self.sampling_events.values()
                    if se["trip_id"] == trip_id
                ],
                "invertebrate_samples": [
                    inv for inv in self.invertebrate_samples.values()
                    if inv["event_id"] in [se["event_id"] for se in self.sampling_events.values() if se["trip_id"] == trip_id]
                ],
                "water_samples": [
                    ws for ws in self.water_samples.values()
                    if ws["event_id"] in [se["event_id"] for se in self.sampling_events.values() if se["trip_id"] == trip_id]
                ],
                "chemical_analyses": [
                    ca for ca in self.chemical_analyses.values()
                    if ca["sample_id"] in [ws["sample_id"] for ws in self.water_samples.values() if ws["event_id"] in [se["event_id"] for se in self.sampling_events.values() if se["trip_id"] == trip_id]]
                ]
            }
            return report
        return {"error": "Field Trip ID not found"}

# --- Example Usage ---
if __name__ == "__main__":
    ta_system = LimnologyTASystem()

    # Create a course and add students
    print("=== Course Management ===")
    print(ta_system.create_course("Limnology (NR 145)", "Fall 2023", "Dr. Johnson", ["Alice", "Bob", "Charlie"]))

    # Schedule lab sessions
    print("\n=== Lab Sessions ===")
    print(ta_system.schedule_lab_session("COURSE1", "2023-09-10", "Water Sampling Techniques", "UVM Lab", ["Niskin Bottle Demo", "Secchi Disc Usage"]))
    print(ta_system.add_lab_activity("LAB1", "pH and Conductivity Testing"))
    print(ta_system.conduct_lab_session("LAB1"))

    # Schedule and conduct a field trip
    print("\n=== Field Trips ===")
    print(ta_system.schedule_field_trip("COURSE1", "2023-09-15", "Lake Champlain", "Marcelle Melosira"))
    print(ta_system.use_sampling_gear("TRIP1", "Niskin Bottle"))
    print(ta_system.use_sampling_gear("TRIP1", "Plankton Net"))
    print(ta_system.use_sampling_gear("TRIP1", "Secchi Disc"))
    print(ta_system.conduct_field_trip("TRIP1"))

    # Record sampling events
    print("\n=== Sampling Events ===")
    print(ta_system.record_sampling_event("TRIP1", "Station A", "Niskin Bottle", [
        {"type": "Water", "depth": "5m", "volume": "1L"},
        {"type": "Water", "depth": "10m", "volume": "1L"}
    ]))
    print(ta_system.record_sampling_event("TRIP1", "Station B", "Plankton Net", [
        {"type": "Zooplankton", "depth": "0-1m", "duration": "5 min"}
    ]))

    # Collect and identify invertebrates
    print("\n=== Invertebrate Sampling ===")
    print(ta_system.collect_invertebrate_sample("EVENT1", "Station A", ["Daphnia pulex", "Cyclops"]))
    print(ta_system.collect_invertebrate_sample("EVENT2", "Station B", ["Water Flea", "Rotifer"]))
    print(ta_system.identify_organisms("INV1", "STU1", [
        {"common_name": "Water Flea", "scientific_name": "Daphnia pulex", "taxa_group": "Zooplankton", "confidence": "High"},
        {"common_name": "Cyclops", "scientific_name": "Cyclops sp.", "taxa_group": "Zooplankton", "confidence": "Medium"}
    ]))

    # Collect water samples and perform chemical analysis
    print("\n=== Water Sampling and Chemical Analysis ===")
    print(ta_system.collect_water_sample("EVENT1", "Station A", ["Phosphorus", "Nitrogen", "pH"]))
    print(ta_system.perform_chemical_analysis("WATER1", "Phosphorus", 45.2, "Spectrophotometer"))
    print(ta_system.perform_chemical_analysis("WATER1", "Nitrogen", 2.1, "Colorimetry"))
    print(ta_system.perform_chemical_analysis("WATER1", "pH", 7.8, "pH Meter"))

    # Record student attendance and grades
    print("\n=== Student Support ===")
    print(ta_system.record_attendance("LAB1", "STU1", "Present"))
    print(ta_system.record_attendance("LAB1", "STU2", "Present"))
    print(ta_system.record_grade("STU1", "Lab Report 1", 92.5))
    print(ta_system.record_grade("STU2", "Lab Report 1", 88.0))

    # Schedule office hours
    print(ta_system.schedule_office_hours("2023-09-20", ["STU1", "STU3"], ["Water Sampling Questions", "Invertebrate ID Help"]))
    print(ta_system.add_office_hours_notes("OH1", "Discussed Niskin bottle technique with STU1. Reviewed zooplankton ID with STU3."))

    # Generate reports
    print("\n=== Course Report ===")
    course_report = ta_system.generate_course_report("COURSE1")
    for key, value in course_report.items():
        print(f"{key}: {value}")

    print("\n=== Student Report for Alice ===")
    student_report = ta_system.generate_student_report("STU1")
    for key, value in student_report.items():
        print(f"{key}: {value}")

    print("\n=== Field Trip Report for Lake Champlain ===")
    trip_report = ta_system.generate_field_trip_report("TRIP1")
    for key, value in trip_report.items():
        print(f"{key}: {value}")
