import React, { useState, useEffect } from "react";
import { apiURL } from "../util/api";
import SearchInput from "../Search/SearchInput";
import FilterCountry from "../FilterCountry/FilterCountry";
import { Link } from "react-router-dom";
import axios from 'axios';

const AllCountries = () => {
  const [countries, setCountries] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  // const getAllCountries = async () => {
  //   try {
  //     const res = await fetch('http://localhost:8000/');

  //     if (!res.ok) throw new Error("Something went wrong!");

  //     const data = await res.json();

  //     console.log(data);

  //     setCountries(data);

  //     setIsLoading(false);
  //   } catch (error) {
  //     setIsLoading(false);
  //     setError(error.message);
  //   }
  // };

  const getCountryByName = async (countryName) => {
    try {
      const res = await fetch(`http://localhost:8000/countries?search=${countryName}`);
      if (!res.ok) throw new Error("Not found any country!");

      const data = await res.json();
      setCountries(data);

      setIsLoading(false);
    } catch (error) {
      setIsLoading(false);
      setError(error.message);
    }
  };

  // const getCountryByRegion = async (regionName) => {
  //   try {
  //     const res = await fetch(`${apiURL}/region/${regionName}`);

  //     if (!res.ok) throw new Error("Failed..........");

  //     const data = await res.json();
  //     setCountries(data);

  //     setIsLoading(false);
  //   } catch (error) {
  //     setIsLoading(false);
  //     setError(false);
  //   }
  // };

  useEffect(() => {
    const fetchData = async () => {
      try {
        // const response = await axios.get(`${apiURL}/all`);
        console.log("dsdsd")
        const response = await axios.get("http://localhost:8000/countries");
        console.log(response)
        setCountries(response.data);
        setIsLoading(false);
      } catch (error) {
        setError(error);
        // setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="all__country__wrapper">
      <div className="country__top">
        <div className="search">
          <SearchInput onSearch={getCountryByName} />
        </div>

        <div className="filter">
          <FilterCountry onSelect={getCountryByRegion} />
        </div>
      </div>

      <div className="country__bottom">
        {isLoading && !error && <h4>Loading........</h4>}
        {error && !isLoading && <h4>{error}</h4>}

        {countries?.map((country, index) => (
          <Link to={`/country/${country.name}`} key={index}>
            <div className="country__card">
              <div className="country__img">
                <img src={country.flag} alt="" />
              </div>

              <div className="country__data">
                <h3>{country.name}</h3>
                <h6>
                  {" "}
                  Population:{" "}
                  {new Intl.NumberFormat().format(country.population)}
                  people
                </h6>
                <h6>
                  {" "}
                  Capitals:{" "}
                  {country.capitals.map((capital, index) => (
                    <span key={index}>{capital.name}</span>

                  ))}
                </h6>
                <h6>
                  {" "}
                  Currencies:{" "}
                  {country.currencies.map((currency, index) => (
                    <span key={index}>{currency.name}</span>
                  ))}
                </h6>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default AllCountries;
