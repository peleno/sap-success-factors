import React, { useState, useEffect } from "react";
import { VacancyItem } from "./VacancyItem/VacancyItem";
import { VacanciesContainer, StyledButton } from "./Home.styled";

import { useNavigate } from "react-router-dom";
import { getAllVacancies } from "../api/Api";
const Home = () => {
    const [vacancies, setVacancies] = useState([]);
    const navigate = useNavigate();
    function goToCreateVacancyPage() {
        navigate("/create_vacancy");
    }

    useEffect(() => {
        getAllVacancies().then((res) => setVacancies(res));
        console.log();
    }, []);

    return (
        <VacanciesContainer>
            {vacancies.map((vacancy) => (
                <VacancyItem vacancy={vacancy}></VacancyItem>
            ))}
            <StyledButton onClick={goToCreateVacancyPage}>Add new vacancy</StyledButton>
        </VacanciesContainer>
    );
};

export default Home;
