import React, { useState } from "react";

import "antd/dist/antd.css";
import { Container } from "./EditVacancy.styled";
import { Input, Button } from "antd";
import { updateVacancy } from "../api/Api";
import { useNavigate, useLocation } from "react-router-dom";

export const EditVacancy = () => {
    const [vacancyName, setVacancyName] = useState("");
    const [vacancyDescription, setVacancyDescription] = useState("");
    const [vacancySalary, setVacancySalary] = useState("");
    const [vacancyExperience, setVacancyExpirience] = useState("");
    const [vacancyIsUrgent, setVacancyIsUrgent] = useState("");
    const [vacancySeniority, setVacancySeniority] = useState("");
    const [vacancyDirection, setVacancyDirection] = useState("");
    let navigate = useNavigate();
    const location = useLocation();
    const oldVacancy = location.state;
    console.log(oldVacancy);
    function sendPutRequest() {
        const vacancy = {
            id: oldVacancy.id,
            name: vacancyName,
            description: vacancyDescription,
            salary: vacancySalary,
            experience: vacancyExperience,
            is_urgent: vacancyIsUrgent,
            seniority: vacancySeniority,
            direction: vacancyDirection
        };
        console.log(vacancy);
        updateVacancy(vacancy);
        navigate(-1);
    }
    return (
        <Container>
            <Input
                defaultValue={oldVacancy.name}
                // value={vacancyName}
                onChange={(e) => setVacancyName(e.target.value)}
            ></Input>
            <Input
                defaultValue={oldVacancy.description}
                // value={vacancyDescription}
                onChange={(e) => setVacancyDescription(e.target.value)}
            ></Input>
            <Input
                defaultValue={oldVacancy.salary}
                // value={vacancySalary}
                onChange={(e) => setVacancySalary(e.target.value)}
            ></Input>
            <Input
                defaultValue={oldVacancy.experience}
                // value={vacancyExperience}
                onChange={(e) => setVacancyExpirience(e.target.value)}
            ></Input>
            <Input
                defaultValue={oldVacancy.is_urgent}
                // value={vacancyIsUrgent}
                onChange={(e) => setVacancyIsUrgent(e.target.value)}
            ></Input>
            <Input
                defaultValue={oldVacancy.seniority}
                // value={vacancySeniority}
                onChange={(e) => setVacancySeniority(e.target.value)}
            ></Input>
            <Input
                defaultValue={oldVacancy.direction}
                // value={vacancyDirection}
                onChange={(e) => setVacancyDirection(e.target.value)}
            ></Input>
            <Button onClick={sendPutRequest}>Update vacancy</Button>
        </Container>
    );
};
