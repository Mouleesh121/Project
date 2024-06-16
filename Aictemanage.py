import random

MAX_CANDIDATES = 100
MAX_COLLEGES = 3
MAX_COURSES = 3
MAX_COURSE_NAME = 60

class Course:
    def __init__(self, courseName, minEntranceScore, maxEntranceScore, maxSeats):
        self.courseName = courseName
        self.minEntranceScore = minEntranceScore
        self.maxEntranceScore = maxEntranceScore
        self.maxSeats = maxSeats
        self.admittedCandidates = 0

class College:
    def __init__(self, collegeName, hasAICTEApproval, ranking, courses):
        self.collegeName = collegeName
        self.hasAICTEApproval = hasAICTEApproval
        self.ranking = ranking
        self.courses = courses

class Candidate:
    def __init__(self, candidateId, candidateName, entranceExamScore, selectedCourse, admissionStatus):
        self.candidateId = candidateId
        self.candidateName = candidateName
        self.entranceExamScore = entranceExamScore
        self.selectedCourse = selectedCourse
        self.admissionStatus = admissionStatus

def welcomeMessage():
    print("\n1. Register for Counseling")
    print("2. Conduct Entrance Exam")
    print("3. Display Colleges with AICTE Approval")
    print("4. Display Results")
    print("5. Admit Candidates")
    print("6. Exit")

def registerForCounseling(candidates):
    print("Step 1: Register for AICTE Counseling")
    
    candidateName = input("Enter candidate name: ")
    selectedCourse = input("Enter preferred course: ")

    candidateId = len(candidates) + 1
    candidate = Candidate(candidateId, candidateName, 0.0, selectedCourse, 0)
    candidates.append(candidate)

    print("Candidate registered successfully!")

def conductEntranceExam(candidates):
    print("Step 2: Conduct Entrance Exam")

    for candidate in candidates:
        candidate.entranceExamScore = 50.0 + random.random() * 30.0
        print(f"Candidate {candidate.candidateName} - Exam Score: {candidate.entranceExamScore:.2f}")
        suggestCourses(candidate)

def suggestCourses(candidate):
    print(f"Suggested Courses for {candidate.candidateName} (Score: {candidate.entranceExamScore:.2f}):")
    if candidate.entranceExamScore > 75.0:
        print("- Course CSE  (High-Demand)")
        print("- Course AIML (High-Demand)")
    else:
        print("- Course IT (General)")
        print("- Course CIVIL (General)")

def displayCollegesWithAICTEApproval(colleges):
    print("Step 3: Display Colleges with AICTE Approval")
    
    print("Colleges with AICTE Approval:")
    for college in colleges:
        if college.hasAICTEApproval:
            print(f"{college.ranking}. {college.collegeName}")

    selectedCollege = int(input("Enter the ranking of the AICTE-approved college to view available seats: "))

    if 1 <= selectedCollege <= len(colleges) and colleges[selectedCollege - 1].hasAICTEApproval:
        college = colleges[selectedCollege - 1]
        print(f"\nAvailable Seats in {college.collegeName}:")
        print("Course          Max Seats   Admitted Candidates")
        for course in college.courses:
            print(f"{course.courseName:<15}{course.maxSeats:<11}{course.admittedCandidates}")
    else:
        print("Invalid college ranking or selected college is not AICTE-approved.")

def displayResults(candidates):
    print("Step 4: Display Results")

    print("Candidate ID   Candidate Name   Course   Exam Score   Status")
    for candidate in candidates:
        status = "Admitted" if candidate.admissionStatus == 1 else "Not Admitted"
        print(f"{candidate.candidateId:<13}{candidate.candidateName:<16}{candidate.selectedCourse:<9}{candidate.entranceExamScore:<14.2f}{status}")

def admitCandidates(candidates, colleges):
    print("Step 5: Admit Candidates")

    for candidate in candidates:
        admitted = False
        for college in colleges:
            for course in college.courses:
                if (course.minEntranceScore <= candidate.entranceExamScore <= course.maxEntranceScore and
                        course.admittedCandidates < course.maxSeats and college.hasAICTEApproval):
                    candidate.admissionStatus = 1
                    course.admittedCandidates += 1
                    print(f"Candidate {candidate.candidateName} has been admitted to {college.collegeName} - {course.courseName}.")
                    admitted = True
                    break
            if admitted:
                break

        if not admitted:
            print(f"Candidate {candidate.candidateName} has not met the admission criteria for any course.")

def exitCounseling():
    print("Thank you for using the AICTE Counseling Management System!")

def main():
    candidates = []

    colleges = [
        College("K.S.Rangasamy College Of Technology", 1, 1, [
            Course("Course-CSE", 60.0, 100.0, 50), 
            Course("Course 2", 65.0, 100.0, 60), 
            Course("Course 3", 70.0, 100.0, 40)
        ]),
        College("Kongu Engineering College", 1, 2, [
            Course("Course IT", 65.0, 100.0, 30), 
            Course("Course 5", 68.0, 100.0, 25), 
            Course("Course 6", 72.0, 100.0, 35)
        ]),
        College("Nandha Engineering College", 1, 3, [
            Course("Course-CIVIL", 70.0, 100.0, 20), 
            Course("Course 8", 75.0, 100.0, 15), 
            Course("Course 9", 80.0, 100.0, 25)
        ]),
    ]

    print("Welcome to AICTE Counseling Management System!")

    choice = 0
    while choice != 6:
        welcomeMessage()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            registerForCounseling(candidates)
        elif choice == 2:
            conductEntranceExam(candidates)
        elif choice == 3:
            displayCollegesWithAICTEApproval(colleges)
        elif choice == 4:
            displayResults(candidates)
        elif choice == 5:
            admitCandidates(candidates, colleges)
        elif choice == 6:
            exitCounseling()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
