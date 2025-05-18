import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../Profile/Profile.css";
import logo from "../../assets/Images/logo.svg";

const Profile = () => {
  const navigate = useNavigate();
  const [profileData, setProfileData] = useState(null);
  const [grades, setGrades] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("token");

    // if (!token) {
    //   navigate("/");
    //   return;
    // }

    fetch("http://127.0.0.1:8000/student/profile", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(async (res) => {
        if (!res.ok)
          throw new Error("Оишбка при попытке получить основную информацию");
        const data = await res.json();
        setProfileData(data);
      })
      .catch(() => {
        // localStorage.removeItem("token");
        // navigate("/");
        setProfileData({
          full_name: "Иванов Иван Иванович",
          group: "М8О-202Б-23",
          education_form: "Очная",
          status: "Продолжает обучение",
          email: "ivanov@example.com",
        });
      });

    fetch("http://127.0.0.1:8000/docs/student/grades", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(async (res) => {
        if (!res.ok)
          throw new Error("Ошибка при попытке получить информацию об оценках");
        const gradeData = await res.json();
        setGrades(gradeData);
      })
      .catch(() => {
        setGrades([
          { semester: 1, subject: "Математика", grade: 5 },
          { semester: 1, subject: "Физика", grade: 4 },
          { semester: 2, subject: "Информатика", grade: 5 },
        ]);
      });
  }, [navigate]);

  if (!profileData) return <div className="loading">Загрузка...</div>;

  return (
    <div className="profile_container">
      <button
        className="logout_button"
        onClick={() => {
          localStorage.removeItem("token");
          navigate("/");
        }}
      >
        Выйти
      </button>
      {/* основная инфа */}
      <div className="profile_wrapper">
        <div className="profile_header">
          <div className="profile_logo">
            <img src={logo} alt="Логотип" />
          </div>
          <h1 className="profile_title">Личный кабинет студента</h1>
        </div>

        <div className="student_name">{profileData.full_name}</div>

        <div className="profile_info">
          <div className="profile_row">
            <div className="profile_field">
              <div className="label">Группа</div>
              <div className="value_box">{profileData.group}</div>
            </div>
            <div className="profile_field">
              <div className="label">Форма обучения</div>
              <div className="value_box">{profileData.education_form}</div>
            </div>
          </div>

          <div className="profile_row">
            <div className="profile_field">
              <div className="label">Статус</div>
              <div className="value_box">{profileData.status}</div>
            </div>
            <div className="profile_field">
              <div className="label">Email</div>
              <div className="value_box">{profileData.email}</div>
            </div>
          </div>
        </div>

        <div className="separator"></div>
        {/* Таблица */}
        {grades.length > 0 && (
          <div className="grades_section">
            <h2 className="grades_title">Табель успеваемости</h2>
            <table className="grades_table">
              <thead>
                <tr>
                  <th>Семестр</th>
                  <th>Дисциплина</th>
                  <th>Оценка</th>
                </tr>
              </thead>
              <tbody>
                {grades.map((grade, index) => (
                  <tr key={index}>
                    <td>{grade.semester}</td>
                    <td>{grade.subject}</td>
                    <td>{grade.grade}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default Profile;
