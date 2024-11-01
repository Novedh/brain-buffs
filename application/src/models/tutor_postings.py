from src.config import get_db_connection


def search_tutor_postings(selected_subject, search_text):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, s.name, u.name AS tutor_name
    FROM tutor_posting t
    JOIN subject s ON t.subject_id = s.id
    JOIN user u ON t.user_id = u.id
    WHERE (%s = 'All' OR s.name = %s)
    AND CONCAT(t.description, ' ', t.class_number, ' ', u.name) LIKE %s
    """
    params = (selected_subject, selected_subject, f"%{search_text}%")
    cursor.execute(query, params)
    tutor_postings = cursor.fetchall()
    cursor.close()
    conn.close()

    return tutor_postings


def get_tutor_count(selected_subject, search_text):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    SELECT COUNT(*)
    FROM tutor_posting t
    JOIN subject s ON t.subject_id = s.id
    JOIN user u ON t.user_id = u.id
    WHERE (%s = 'All' OR s.name = %s)
    AND CONCAT(t.description, ' ', t.class_number, ' ', u.name) LIKE %s
    """
    params = (selected_subject, selected_subject, f"%{search_text}%")
    cursor.execute(query, params)
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count


def is_valid_subject(selected_subject, subjects):
    valid_subjects = [subject["name"] for subject in subjects]
    return selected_subject == "All" or selected_subject in valid_subjects
