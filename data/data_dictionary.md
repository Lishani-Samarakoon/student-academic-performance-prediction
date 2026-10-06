# Data Dictionary

## Raw Columns (Survey)
| Column | Description | Values |
|--------|-------------|--------|
| Consent | Agreement to participate | Yes / No |
| Age group | Age bracket | 18-20, 21-23, 24-26, 27+ |
| Gender | Self-reported gender | Male / Female / Prefer not to say |
| University | Institution name | Various |
| Field of study | Degree field | Various |
| Year of study | Current year | Year 1-4 |
| Family income | Monthly income | LKR ranges |
| Current GPA | Most recent GPA | Below 2.00 to 3.50-4.00 |
| Workload | Self-rated academic workload | Very light to Very heavy |
| Assignment frequency | Assignments/week | 0-1 to 6+ |
| Self-study hours | Weekly study hours | Ranges |
| Work hours | Weekly part-time hours | Ranges |
| Attendance | Attendance % | Below 50% to 90-100% |

## Processed Columns
| Column | Type | Description |
|--------|------|-------------|
| label | Binary | 0 = Low (GPA < 3.0), 1 = High (GPA >= 3.0) |
| attend_num | Numeric | Attendance % midpoint |
| workload_num | Ordinal | 1=Very light ... 5=Very heavy |
| assign_num | Ordinal | 1=0-1 ... 4=6+ assignments |
| study_num | Numeric | Weekly self-study hours |
| work_num | Numeric | Weekly work hours (0 if no job) |

## Label Rule
- GPA < 3.0  -> 0 (Low performance)
- GPA >= 3.0 -> 1 (High performance)
