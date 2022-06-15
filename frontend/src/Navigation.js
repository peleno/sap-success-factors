import React from "react";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { CreateVacancy } from "./CreateVacancy/CreateVacancy.js";
import { EditVacancy } from "./EditVacancy/EditVacancy.js";
// import { VacancyDetails } from "./Details/VacancyDetails";
import Home from "./Home/Home";
export const AppRouter = () => {
    return (
        <Router>
            <Routes>
                {/* <Route path="/vacancy/:vacancyId/monitor">
                    <VacancyDetails></VacancyDetails>
                </Route> */}
                <Route path="/vacancy/:vacancyId/edit" element={<EditVacancy/>}/>
                <Route path="/create_vacancy" element={<CreateVacancy/>}/>
                <Route path="/" element={<Home/>}/>
            </Routes>
        </Router>
    );
};
