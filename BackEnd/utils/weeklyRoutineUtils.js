const calculateRoutineEndDate = (startDate) => {
  const endDate = new Date(startDate);
  endDate.setDate(endDate.getDate() + 7);
  return endDate;
};


export const updateStatusRoutine = async (routine) => {
  const routineEndDate = calculateRoutineEndDate(routine.start_date)

  if (new Date() > routineEndDate) {
    routine.status = routine.progress >= 100 ? "completed" : "expired";
    await routine.save();
    return true;
  }
  return false;
};
