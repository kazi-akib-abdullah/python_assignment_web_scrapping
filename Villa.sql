-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 08, 2021 at 08:37 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parsingData`
--

-- --------------------------------------------------------

--
-- Table structure for table `Villa`
--

CREATE TABLE `Villa` (
  `Name` varchar(250) NOT NULL,
  `Sleeps` varchar(30) DEFAULT NULL,
  `Bedroom` varchar(30) DEFAULT NULL,
  `Bathroom` varchar(30) DEFAULT NULL,
  `Price` varchar(10) DEFAULT NULL,
  `Image1` varchar(500) DEFAULT NULL,
  `Image2` varchar(500) DEFAULT NULL,
  `Image3` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Villa`
--

INSERT INTO `Villa` (`Name`, `Sleeps`, `Bedroom`, `Bathroom`, `Price`, `Image1`, `Image2`, `Image3`) VALUES
('1 bedroom house right on King Street in the heart of downtown Boone', 'Sleeps 4', '2 Bedrooms', '1 Bathroom', '$176', '\"https://media.vrbo.com/lodging/20000000/19630000/19625100/19625088/7ad5e032.c6.jpg\"', '\"https://media.vrbo.com/lodging/20000000/19630000/19625100/19625088/b6868d30.c6.jpg\"', '\"https://media.vrbo.com/lodging/20000000/19630000/19625100/19625088/27c32eab.c6.jpg\"'),
('Close to Appalachian State University Campus', 'Sleeps 6', '2 Bedrooms', '2 Bathrooms', '$94', '\"https://media.vrbo.com/lodging/31000000/30230000/30228800/30228791/88dd688d.c6.jpg\"', '\"https://media.vrbo.com/lodging/31000000/30230000/30228800/30228791/0d4450e1.c6.jpg\"', '\"https://media.vrbo.com/lodging/31000000/30230000/30228800/30228791/883ae1ea.c6.jpg\"'),
('Newly Renovated and Located Near Downtown, ASU and Shopping.', 'Sleeps 6', '3 Bedrooms', '3 Bathrooms', '$185', '\"https://media.vrbo.com/lodging/59000000/58050000/58049300/58049204/3177542f.c6.jpg\"', '\"https://media.vrbo.com/lodging/59000000/58050000/58049300/58049204/66ba9f6c.c6.jpg\"', '\"https://media.vrbo.com/lodging/59000000/58050000/58049300/58049204/11c71a0a.c6.jpg\"'),
('Peace of Mind - Pet Friendly Mountain Home, 2 sided Fireplace 15 minutes to Boone!', 'Sleeps 6', '3 Bedrooms', '3 Bathrooms', '$191', '\"https://media.vrbo.com/lodging/34000000/33310000/33305300/33305274/13e31be9.c6.jpg\"', '\"https://media.vrbo.com/lodging/34000000/33310000/33305300/33305274/eff583d0.c6.jpg\"', '\"https://media.vrbo.com/lodging/34000000/33310000/33305300/33305274/f45cb545.c6.jpg\"'),
('Renovated Mountain Home, 5 Mins to Downtown Boone!', 'Sleeps 5', '2 Bedrooms', '2 Bathrooms', '$208', '\"https://media.vrbo.com/lodging/33000000/32710000/32706100/32706063/920d02b2.c6.jpg\"', '\"https://media.vrbo.com/lodging/33000000/32710000/32706100/32706063/84c79d94.c6.jpg\"', '\"https://media.vrbo.com/lodging/33000000/32710000/32706100/32706063/a2d78df0.c6.jpg\"'),
('Urban Oasis on King Street!', 'Sleeps 2', 'Studio', '1 Bathroom', '$120', '\"https://media.vrbo.com/lodging/71000000/70290000/70282800/70282719/cf5d20ca.c6.jpg\"', '\"https://media.vrbo.com/lodging/71000000/70290000/70282800/70282719/49c4cfa0.c6.jpg\"', '\"https://media.vrbo.com/lodging/71000000/70290000/70282800/70282719/6d6aaba8.c6.jpg\"');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Villa`
--
ALTER TABLE `Villa`
  ADD PRIMARY KEY (`Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
