# 프로젝트: Learning Management System API 만들기

  

## 목표: LMS 사이트를 위한 REST API 만들기

  

## 요구사항:

  

팀장 ALEX: 우리는 학생들의 수강현황을 파악하기 위한 LMS를 만들거야

과목은 시범적으로 국어, 영어, 수학만 사용할 것이지만 추후에 다른 과목들도 추가할거야

우리 서비스에는 강사들이 있어. 강사들은 담당 교과목이 존재하고, 교과목마다 여러 개의 강의를 진행할거야.학생들은 그 강의를 수강할거야.

  
  

- 요구사항 재정의: 해당 LMS는 '학생이 수강한 강의 확인하기'를 핵심기능으로 갖는다.

- 프로젝트 진행 범위: '강의 수강현황 조회'기능 구현

  

## ERD 문서(이미지 파일)

  
  ![[LMS_프로젝트.drawio.png]]

## LMS 사이트 기능

  

- 학생: 강의 수강하기

- 강사: 강의를 수강하는 학생 관리하기

  

## Entity Relationship Diagram(ERD)

ERD 문서: https://documenter.getpostman.com/view/33627655/2sA35D53Jx

 - 학생(Student)

   - `student:` 닉네임

   - `grade`: 학년

 - 강의(Lecture)

   - `teacher`: 강사

   - `students`: 학생ID

   - `title`: 강의명

   - `grade`: 학년

   - `subgect`: 과목

 - 강사(Teacher)

   - `grade`: 학년

   - `subject`: 과목

## 관계 설명

- 학생과 강의는 M:N관계를 맺는다. 따라서 중간에 중계 테이블로 '강의 수강'이 필요하다.

- 학생과 강의 수강은 1:N관계를 맺는다(Foreign Key: 학생ID)

  학생ID는 로그인시 사용하는 ID를 의미한다. 모델에 ID 필드를 만들지 않은 이유는 jango에서 모델 생성시 자동으로 id를 할당하는 것을 사용할 것이기 때문이다.

- 강의와 강의 수강은 1:N관계를 맺는다.(Foreign Key: 강의ID)

- 강사와 강의는 1:N관계를 맺는다.(Foreign Key: 강사 ID)

  
  

## REST API 구현 기능

- 한명의 학생이 수강 신청한 모든 강의 data 보여주기

- 특정 강의를 수강한 모든 학생 data 보여주기