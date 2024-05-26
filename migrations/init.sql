--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg120+1)
-- Dumped by pg_dump version 15.7 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: data_first; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.data_first (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.data_first OWNER TO root;

--
-- Name: data_second; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.data_second (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.data_second OWNER TO root;

--
-- Name: data_third; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.data_third (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.data_third OWNER TO root;

--
-- Data for Name: data_first; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public.data_first (id, name) VALUES (1, 'd');
INSERT INTO public.data_first (id, name) VALUES (2, 'c');
INSERT INTO public.data_first (id, name) VALUES (3, 'a');
INSERT INTO public.data_first (id, name) VALUES (4, 'd');
INSERT INTO public.data_first (id, name) VALUES (5, 'd');
INSERT INTO public.data_first (id, name) VALUES (6, 'b');
INSERT INTO public.data_first (id, name) VALUES (7, 'c');
INSERT INTO public.data_first (id, name) VALUES (8, 'b');
INSERT INTO public.data_first (id, name) VALUES (9, 'b');
INSERT INTO public.data_first (id, name) VALUES (10, 'a');
INSERT INTO public.data_first (id, name) VALUES (31, 'c');
INSERT INTO public.data_first (id, name) VALUES (32, 'g');
INSERT INTO public.data_first (id, name) VALUES (33, 'b');
INSERT INTO public.data_first (id, name) VALUES (34, 'a');
INSERT INTO public.data_first (id, name) VALUES (35, 'e');
INSERT INTO public.data_first (id, name) VALUES (36, 'f');
INSERT INTO public.data_first (id, name) VALUES (37, 'b');
INSERT INTO public.data_first (id, name) VALUES (38, 'c');
INSERT INTO public.data_first (id, name) VALUES (39, 'd');
INSERT INTO public.data_first (id, name) VALUES (40, 'a');


--
-- Data for Name: data_second; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public.data_second (id, name) VALUES (11, 'g');
INSERT INTO public.data_second (id, name) VALUES (12, 'd');
INSERT INTO public.data_second (id, name) VALUES (13, 'f');
INSERT INTO public.data_second (id, name) VALUES (14, 'd');
INSERT INTO public.data_second (id, name) VALUES (15, 'a');
INSERT INTO public.data_second (id, name) VALUES (16, 'a');
INSERT INTO public.data_second (id, name) VALUES (17, 'd');
INSERT INTO public.data_second (id, name) VALUES (18, 'd');
INSERT INTO public.data_second (id, name) VALUES (19, 'c');
INSERT INTO public.data_second (id, name) VALUES (20, 'd');
INSERT INTO public.data_second (id, name) VALUES (41, 'g');
INSERT INTO public.data_second (id, name) VALUES (42, 'a');
INSERT INTO public.data_second (id, name) VALUES (43, 'g');
INSERT INTO public.data_second (id, name) VALUES (44, 'g');
INSERT INTO public.data_second (id, name) VALUES (45, 'd');
INSERT INTO public.data_second (id, name) VALUES (46, 'c');
INSERT INTO public.data_second (id, name) VALUES (47, 'g');
INSERT INTO public.data_second (id, name) VALUES (48, 'a');
INSERT INTO public.data_second (id, name) VALUES (49, 'd');
INSERT INTO public.data_second (id, name) VALUES (50, 'c');


--
-- Data for Name: data_third; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO public.data_third (id, name) VALUES (21, 'g');
INSERT INTO public.data_third (id, name) VALUES (22, 'd');
INSERT INTO public.data_third (id, name) VALUES (23, 'f');
INSERT INTO public.data_third (id, name) VALUES (24, 'b');
INSERT INTO public.data_third (id, name) VALUES (25, 'b');
INSERT INTO public.data_third (id, name) VALUES (26, 'a');
INSERT INTO public.data_third (id, name) VALUES (27, 'c');
INSERT INTO public.data_third (id, name) VALUES (28, 'd');
INSERT INTO public.data_third (id, name) VALUES (29, 'c');
INSERT INTO public.data_third (id, name) VALUES (30, 'a');
INSERT INTO public.data_third (id, name) VALUES (51, 'c');
INSERT INTO public.data_third (id, name) VALUES (52, 'a');
INSERT INTO public.data_third (id, name) VALUES (53, 'b');
INSERT INTO public.data_third (id, name) VALUES (54, 'g');
INSERT INTO public.data_third (id, name) VALUES (55, 'b');
INSERT INTO public.data_third (id, name) VALUES (56, 'e');
INSERT INTO public.data_third (id, name) VALUES (57, 'c');
INSERT INTO public.data_third (id, name) VALUES (58, 'g');
INSERT INTO public.data_third (id, name) VALUES (59, 'f');
INSERT INTO public.data_third (id, name) VALUES (60, 'a');


--
-- Name: data_first data_first_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.data_first
    ADD CONSTRAINT data_first_pkey PRIMARY KEY (id);


--
-- Name: data_second data_second_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.data_second
    ADD CONSTRAINT data_second_pkey PRIMARY KEY (id);


--
-- Name: data_third data_third_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.data_third
    ADD CONSTRAINT data_third_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

