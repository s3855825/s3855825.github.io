CREATE TABLE IF NOT EXISTS Students (
    student_id VARCHAR(7) NOT NULL UNIQUE PRIMARY KEY,
    student_name VARCHAR(20) NOT NULL UNIQUE,
    credit_score FLOAT
);

CREATE TABLE IF NOT EXISTS Waitlists (
    waitlist_id INT PRIMARY KEY,
    student_id VARCHAR(7),
    FOREIGN KEY (student_id)
        REFERENCES Students (student_id)
);

CREATE TABLE IF NOT EXISTS Posts (
    post_id INT PRIMARY KEY,
    message VARCHAR(140),
    waitlist_id INT,
    poster_id VARCHAR(7),
    url VARCHAR(50),
    FOREIGN KEY (waitlist_id)
        REFERENCES Waitlists (waitlist_id),
    FOREIGN KEY (poster_id)
        REFERENCES Students (student_id)
);

CREATE TABLE IF NOT EXISTS Courses (
    course_id INT PRIMARY KEY,
    course_code VARCHAR(10),
    course_name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS CoursesTaken (
    id INT PRIMARY KEY,
    student_id VARCHAR(7),
    course_id INT,
    semester VARCHAR(10),
    gpa FLOAT,
    FOREIGN KEY (student_id)
        REFERENCES Students (student_id),
    FOREIGN KEY (course_id)
        REFERENCES Courses (course_id)
);

CREATE TABLE IF NOT EXISTS Review (
    id INT PRIMARY KEY,
    student1_id VARCHAR(7),
    student2_id VARCHAR(7),
    score FLOAT,
    FOREIGN KEY (student1_id)
        REFERENCES Students (student_id),
    FOREIGN KEY (student2_id)
        REFERENCES Students (student_id)
);

CREATE TABLE IF NOT EXISTS StudentGroups (
    id INT PRIMARY KEY,
    group_name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS GroupMembers (
    id INT PRIMARY KEY,
    group_id INT,
    student_id VARCHAR(7),
    member_role ENUM('poster', 'member'),
    FOREIGN KEY (group_id)
        REFERENCES StudentGroups (id),
    FOREIGN KEY (student_id)
        REFERENCES Students (student_id)
);

CREATE TABLE IF NOT EXISTS Messages (
    id INT PRIMARY KEY,
    message VARCHAR(140),
    sender_id VARCHAR(7),
    FOREIGN KEY (sender_id)
        REFERENCES Students (student_id)
);


