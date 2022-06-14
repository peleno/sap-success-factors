from data_access.database.session import get_session
from model.hiring_progress import HiringProgress


def select_all_hiring_progresses():
    session = get_session()
    return session.query(HiringProgress).order_by(HiringProgress.id).all()


def create_hiring_progress(hiring_progress: HiringProgress):
    session = get_session()
    session.add(hiring_progress)
    session.commit()


def delete_hiring_progress(hiring_progress_id):
    session = get_session()
    session.query(HiringProgress).filter(HiringProgress.id == hiring_progress_id).delete()
    session.commit()


def update_candidate(new_hiring_progress):
    session = get_session()
    if new_hiring_progress.id is None:
        raise Exception("Id of hiring_progress to be updated is not specified")
    hiring_progress_to_update = session.query(HiringProgress).filter(HiringProgress.id == new_hiring_progress.id).first()
    if new_hiring_progress.hiring_stage is not None:
        hiring_progress_to_update.hiring_stage = new_hiring_progress.hiring_stage
    if new_hiring_progress.recruiter_feedback is not None:
        hiring_progress_to_update.recruiter_feedback = new_hiring_progress.recruiter_feedback
    if new_hiring_progress.technical_interviewer_feedback is not None:
        hiring_progress_to_update.technical_interviewer_feedback = new_hiring_progress.technical_interviewer_feedback
    if new_hiring_progress.technical_test_result is not None:
        hiring_progress_to_update.technical_test_result = new_hiring_progress.technical_test_result
    if new_hiring_progress.english_assessment_result is not None:
        hiring_progress_to_update.english_assessment_result = new_hiring_progress.english_assessment_result
    if new_hiring_progress.manager_feedback is not None:
        hiring_progress_to_update.manager_feedback = new_hiring_progress.manager_feedback
    if new_hiring_progress.candidate_id is not None:
        hiring_progress_to_update.candidate_id = new_hiring_progress.candidate_id
    session.commit()


if __name__ == '__main__':
    for hiring_progress in select_all_hiring_progresses():
        print(hiring_progress)
