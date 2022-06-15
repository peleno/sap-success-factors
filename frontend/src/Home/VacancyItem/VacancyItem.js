import React from "react";
import "antd/dist/antd.css";
import {
    StyledVacancyItem,
    VacancyItemContent,
    DeleteButton,
    EditButton,
} from "./VacancyItem.styled";
import { useNavigate } from "react-router-dom";
import { deleteVacancy } from '../../api/Api';

export const VacancyItem = (props) => {
    const { vacancy } = props;
    let navigate = useNavigate();
    function deleteCurrentVacancy() {
        deleteVacancy(vacancy.id);
        navigate(0);
    }
    function goToEditVacancyPage() {
        navigate("/vacancy/" + vacancy.id + "/edit", {state: vacancy});
    }
    return (
        <StyledVacancyItem>
            <VacancyItemContent>
                <div>Vacancy name</div>
                <div>Salary</div>
                <div>Experience</div>
                <div>Is urgent</div>
                <div>Seniority</div>
                <div>Direction</div>
                <h3>{vacancy.name}</h3>
                <div>{vacancy.salary}</div>
                <div>{vacancy.experience + ' year(s)'}</div>
                <div>{vacancy.is_urgent ? 'Yes' : 'No'}</div>
                <div>{vacancy.seniority}</div>
                <div>{vacancy.direction}</div>
            </VacancyItemContent>
            <EditButton onClick={goToEditVacancyPage}>Edit</EditButton>
            <DeleteButton onClick={deleteCurrentVacancy}>Delete</DeleteButton>
        </StyledVacancyItem>
    );
};
