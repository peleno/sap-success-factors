import React, { useState } from "react";

import "antd/dist/antd.css";
import { Container } from "./CreateVacancy.styled";
import { Input, Button } from "antd";
import { postNewVacancy } from "../api/Api";
import { useNavigate } from "react-router-dom";

export const CreateVacancy = () => {
    const [vacancyName, setVacancyName] = useState("");
    const [vacancyDescription, setVacancyDescription] = useState("");
    const [vacancySalary, setVacancySalary] = useState("");
    const [vacancyExperience, setVacancyExpirience] = useState("");
    const [vacancyIsUrgent, setVacancyIsUrgent] = useState("");
    const [vacancySeniority, setVacancySeniority] = useState("");
    const [vacancyDirection, setVacancyDirection] = useState("");
    let navigate = useNavigate();

    function sendPostRequest() {
        const vacancy = {
            name: vacancyName,
            description: vacancyDescription,
            salary: vacancySalary,
            experience: vacancyExperience,
            is_urgent: vacancyIsUrgent,
            seniority: vacancySeniority,
            direction: vacancyDirection
        };
        console.log(vacancy);
        postNewVacancy(vacancy);
        navigate(-1);
    }
    return (
        <Container>
            <Input
                placeholder="Vacancy name"
                value={vacancyName}
                onChange={(e) => setVacancyName(e.target.value)}
            ></Input>
            <Input
                placeholder="Description"
                value={vacancyDescription}
                onChange={(e) => setVacancyDescription(e.target.value)}
            ></Input>
            <Input
                placeholder="Salary"
                value={vacancySalary}
                onChange={(e) => setVacancySalary(e.target.value)}
            ></Input>
            <Input
                placeholder="Experience"
                value={vacancyExperience}
                onChange={(e) => setVacancyExpirience(e.target.value)}
            ></Input>
            <Input
                placeholder="Is urgent?"
                value={vacancyIsUrgent}
                onChange={(e) => setVacancyIsUrgent(e.target.value)}
            ></Input>
            <Input
                placeholder="Seniority"
                value={vacancySeniority}
                onChange={(e) => setVacancySeniority(e.target.value)}
            ></Input>
            <Input
                placeholder="Direction"
                value={vacancyDirection}
                onChange={(e) => setVacancyDirection(e.target.value)}
            ></Input>
            <Button onClick={sendPostRequest}>Add vacancy</Button>
        </Container>
    );
};
