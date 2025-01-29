
CREATE TABLE "general_farm" (
	"id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL UNIQUE,
	"firstname" varchar(25),
	"lastname" varchar(25),
	"username" varchar(25),
	"email" varchar(50),
	"password" varchar(255),
	"land" varchar(30),
	"region" varchar(50),
	"currency" varchar(20),
	"legal_status" varchar(50),
	"reference_year_data" int,
	"cash_crop" boolean,
	"sows" boolean,
	"pig_finishing" boolean,
	"year" int,
	"farm_id" varchar(255),
	"scenario_id" varchar(255),
	"scenario_name" varchar(255),
	"farm_name" varchar(255),
	"network_pig" boolean,
	"network_beef" boolean,
	"network_crop" boolean,
	"network_horticulture" boolean,
	"network_fish" boolean,
	"network_poultry" boolean,
	PRIMARY KEY("general_id")
);


CREATE TABLE "buildings" (
	"id" uuid NOT NULL UNIQUE,
	"buildings_id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"sow_id" uuid,
	"finishing_id" int,
	-- C
	"sum_annual_depreciation" decimal,
	-- C
	"sum_book_values" decimal,
	"building_name" varchar(255),
	"purchase_year" int,
	-- C/piece
	"purchase_price" decimal,
	-- for tax
	"utilization_period" decimal,
	-- C/piece
	"salvage_value" decimal,
	-- C/piece
	"replacement_value" decimal,
	"enterprise_codes" int,
	"year" int,
	PRIMARY KEY("buildings_id")
);
COMMENT ON COLUMN buildings.sum_annual_depreciation IS 'C';
COMMENT ON COLUMN buildings.sum_book_values IS 'C';
COMMENT ON COLUMN buildings.purchase_price IS 'C/piece';
COMMENT ON COLUMN buildings.utilization_period IS 'for tax';
COMMENT ON COLUMN buildings.salvage_value IS 'C/piece';
COMMENT ON COLUMN buildings.replacement_value IS 'C/piece';


CREATE TYPE "gilts_special_feed_t" AS ENUM ('Special gilt feed', 'Mix of gestation and lactation feed');

CREATE TYPE "boars_special_feed_t" AS ENUM ('Special Boar feed', 'Mix of gestation and lactation feed');

CREATE TABLE "feed_sows" (
	"id" uuid NOT NULL UNIQUE,
	"feed_id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"sow_id" uuid,
	"finishing_id" int,
	-- kg/animal and year
	"sows_gestation_feed" decimal,
	-- kg/animal and year
	"sows_lactation_feed" decimal,
	-- kg/animal and day
	"sows_total_feed_daily" decimal,
	-- kg/year
	"sows_total_feed_yearly" decimal,
	"gilts_special_feed" gilts_special_feed_t,
	-- %
	"gilts_share_gestation_feed" decimal(5,4),
	-- %
	"gilts_share_lactation_feed" decimal(5,4),
	-- kg/animal and year
	"gilts_feed_quantity_yearly" decimal,
	-- kg/year
	"gilts_total_feed_yearly" decimal,
	"boars_special_feed" boars_special_feed_t,
	-- %
	"boars_share_gestation_feed" decimal(5,4),
	-- %
	"boars_share_lactation_feed" decimal(5,4),
	-- kg/animal and year
	"boars_feed_quantity_yearly" decimal,
	-- kg/year
	"boars_total_feed_yearly" decimal,
	-- kg/animal
	"piglet_feed_1" decimal,
	-- kg/animal
	"piglet_feed_2" decimal,
	-- kg/year
	"piglet_feed_quantity_yearly" decimal,
	-- kg/year
	"piglet_total_feed_yearly" decimal,
	"year" int,
	PRIMARY KEY("feed_id")
);
COMMENT ON COLUMN feed_sows.sows_gestation_feed IS 'kg/animal and year';
COMMENT ON COLUMN feed_sows.sows_lactation_feed IS 'kg/animal and year';
COMMENT ON COLUMN feed_sows.sows_total_feed_daily IS 'kg/animal and day';
COMMENT ON COLUMN feed_sows.sows_total_feed_yearly IS 'kg/year';
COMMENT ON COLUMN feed_sows.gilts_share_gestation_feed IS '%';
COMMENT ON COLUMN feed_sows.gilts_share_lactation_feed IS '%';
COMMENT ON COLUMN feed_sows.gilts_feed_quantity_yearly IS 'kg/animal and year';
COMMENT ON COLUMN feed_sows.gilts_total_feed_yearly IS 'kg/year';
COMMENT ON COLUMN feed_sows.boars_share_gestation_feed IS '%';
COMMENT ON COLUMN feed_sows.boars_share_lactation_feed IS '%';
COMMENT ON COLUMN feed_sows.boars_feed_quantity_yearly IS 'kg/animal and year';
COMMENT ON COLUMN feed_sows.boars_total_feed_yearly IS 'kg/year';
COMMENT ON COLUMN feed_sows.piglet_feed_1 IS 'kg/animal';
COMMENT ON COLUMN feed_sows.piglet_feed_2 IS 'kg/animal';
COMMENT ON COLUMN feed_sows.piglet_feed_quantity_yearly IS 'kg/year';
COMMENT ON COLUMN feed_sows.piglet_total_feed_yearly IS 'kg/year';


CREATE TABLE "machines" (
	"id" uuid NOT NULL UNIQUE,
	"machines_id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"sow_id" uuid,
	"finishing_id" int,
	-- C
	"sum_annual_depreciation" decimal,
	-- C
	"sum_book_values" decimal,
	"name" varchar(255),
	"purchase_year" int,
	-- C/piece
	"purchase_price" decimal,
	-- economically
	"utilization_period" decimal,
	-- C/piece
	"salvage_value" decimal,
	-- C/piece
	"replacement_value" decimal,
	"enterprise_code" int,
	"year" int,
	PRIMARY KEY("machines_id")
);
COMMENT ON COLUMN machines.sum_annual_depreciation IS 'C';
COMMENT ON COLUMN machines.sum_book_values IS 'C';
COMMENT ON COLUMN machines.purchase_price IS 'C/piece';
COMMENT ON COLUMN machines.utilization_period IS 'economically';
COMMENT ON COLUMN machines.salvage_value IS 'C/piece';
COMMENT ON COLUMN machines.replacement_value IS 'C/piece';


CREATE TYPE "type_t" AS ENUM ('Manager', 'Executive Staff', 'Tractor Driver', 'Pigman', 'Casual Labour', 'Family Labour', 'Other');

CREATE TABLE "labour" (
	"id" uuid NOT NULL UNIQUE,
	"labour_id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"sow_id" uuid,
	"finishing_id" int,
	"type" type_t,
	-- Number(Anzahl)
	"labor_units" decimal,
	-- per person per year
	"working_hours" decimal,
	-- per person
	"annual_wage_incl_sidecosts" decimal,
	"enterprise_code" int,
	"year" int,
	PRIMARY KEY("labour_id")
);
COMMENT ON COLUMN labour.labor_units IS 'Number(Anzahl)';
COMMENT ON COLUMN labour.working_hours IS 'per person per year';
COMMENT ON COLUMN labour.annual_wage_incl_sidecosts IS 'per person';


CREATE TABLE "cash_crops" (
	"id" uuid NOT NULL UNIQUE,
	"crops_id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"feed_id" uuid,
	-- Set aside, Corn, Wheat, Barley
	"crop_name" varchar(50),
	"year" int,
	PRIMARY KEY("crops_id")
);
COMMENT ON COLUMN cash_crops.crop_name IS 'Set aside, Corn, Wheat, Barley';


CREATE TYPE "production_system_t" AS ENUM ('normal pig finishing', 'additional boar finishing');

CREATE TYPE "production_cyle_t" AS ENUM ('all-in all-out by barn', 'continuous system');

CREATE TABLE "pig_finishing" (
	"id" uuid NOT NULL UNIQUE,
	"finishing_id" int NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"production_system" production_system_t,
	"production_cyle" production_cyle_t,
	-- No. heads
	"animal_places" int,
	-- No heads
	"no_sold_pigs_gi_ba" int,
	"no_sold_em_ic" int,
	-- %
	"share_gi_pigs" decimal(5,4),
	"year" int,
	PRIMARY KEY("finishing_id")
);
COMMENT ON COLUMN pig_finishing.animal_places IS 'No. heads';
COMMENT ON COLUMN pig_finishing.no_sold_pigs_gi_ba IS 'No heads';
COMMENT ON COLUMN pig_finishing.share_gi_pigs IS '%';


CREATE TYPE "productionsystem_t" AS ENUM ('system piglet sales (approx. 8kg)', 'weaner sales (approx. 25-30kg)', 'pure piglet rearing', 'closed system');

CREATE TYPE "production_rhythm_t" AS ENUM ('1-week rhythm', '2-week rhythm', '3-week rhythm', '4-week rhythm', 'none or other rhythm');

CREATE TABLE "sows" (
	"id" uuid NOT NULL UNIQUE,
	"sows_id" uuid NOT NULL UNIQUE,
	"general_id" uuid NOT NULL,
	"productionsystem" productionsystem_t,
	"production_rhythm" production_rhythm_t,
	-- No. heads
	"no_sows_mated_gilts" int,
	-- No. heads
	"no_unserved_gilts" int,
	-- No. heads
	"no_boars" int,
	"total_no_sows_gilts" int,
	"year" int,
	PRIMARY KEY("sows_id")
);
COMMENT ON COLUMN sows.no_sows_mated_gilts IS 'No. heads';
COMMENT ON COLUMN sows.no_unserved_gilts IS 'No. heads';
COMMENT ON COLUMN sows.no_boars IS 'No. heads';


CREATE TABLE "variable_costs_sows" (
	"id" uuid NOT NULL UNIQUE,
	"var_cost_id" uuid NOT NULL UNIQUE,
	-- C/head
	"veterinary_medicine_supplies" decimal,
	-- C/head
	"artificial_insemination" decimal,
	-- C/head
	"pregnancy_check" decimal,
	-- C/head
	"disinfection" decimal,
	-- C/head
	"energy" decimal,
	-- C/head
	"water" decimal,
	-- C/head
	"manure_costs" decimal,
	-- C/head
	"transport_costs" decimal,
	-- C/head
	"specialised_advisors" decimal,
	-- C/head
	"animal_disease_levy" decimal,
	-- C/head
	"carcass_disposal" decimal,
	-- C/head
	"sow_planner" decimal,
	-- C/head
	"maintenance" decimal,
	-- C/head
	"others" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("var_cost_id")
);
COMMENT ON COLUMN variable_costs_sows.veterinary_medicine_supplies IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.artificial_insemination IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.pregnancy_check IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.disinfection IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.energy IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.water IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.manure_costs IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.transport_costs IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.specialised_advisors IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.animal_disease_levy IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.carcass_disposal IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.sow_planner IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.maintenance IS 'C/head';
COMMENT ON COLUMN variable_costs_sows.others IS 'C/head';


CREATE TABLE "fix_costs" (
	"id" uuid NOT NULL UNIQUE,
	"fix_cost_id" uuid NOT NULL UNIQUE,
	-- C/enterprise
	"feed_grinding_preparation" decimal,
	-- C/enterprise
	"insurance" decimal,
	-- C/enterprise
	"cleaning" decimal,
	-- C/enterprise
	"others" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("fix_cost_id")
);
COMMENT ON COLUMN fix_costs.feed_grinding_preparation IS 'C/enterprise';
COMMENT ON COLUMN fix_costs.insurance IS 'C/enterprise';
COMMENT ON COLUMN fix_costs.cleaning IS 'C/enterprise';
COMMENT ON COLUMN fix_costs.others IS 'C/enterprise';


CREATE TABLE "sows_performance" (
	"id" uuid NOT NULL UNIQUE,
	"sows_performance_id" uuid NOT NULL UNIQUE,
	-- piglets/sow/year
	"piglets_born_alive" int,
	-- piglets/sow/year
	"cycles_per_sow_year" int,
	-- days
	"avg_gestation_period" decimal,
	-- days
	"duration_suckling_per_farrowing" decimal,
	-- days
	"dry_sow_days" int,
	-- %
	"rate_insuccesful_insemination" decimal(5,4),
	-- kg LW per head
	"weaning_weights" decimal,
	-- %
	"cull_rate_sows" decimal(5,4),
	-- %
	"cull_rate_boars" decimal(5,4),
	-- %
	"fraction_own_replacement" decimal(5,4),
	-- %
	"annual_sow_mortality" decimal(5,4),
	-- %
	"annual_boar_mortality" decimal(5,4),
	-- %
	"piglet_mortality_weaning" decimal(5,4),
	-- %
	"piglet_mortality_rearing" decimal(5,4),
	-- piglets/sow/year
	"piglets_weaned" decimal,
	-- days
	"avg_duration_piglet_rearing" decimal,
	-- piglets/sow/year
	"reared_piglets" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("sows_performance_id")
);
COMMENT ON COLUMN sows_performance.piglets_born_alive IS 'piglets/sow/year';
COMMENT ON COLUMN sows_performance.cycles_per_sow_year IS 'piglets/sow/year';
COMMENT ON COLUMN sows_performance.avg_gestation_period IS 'days';
COMMENT ON COLUMN sows_performance.duration_suckling_per_farrowing IS 'days';
COMMENT ON COLUMN sows_performance.dry_sow_days IS 'days';
COMMENT ON COLUMN sows_performance.rate_insuccesful_insemination IS '%';
COMMENT ON COLUMN sows_performance.weaning_weights IS 'kg LW per head';
COMMENT ON COLUMN sows_performance.cull_rate_sows IS '%';
COMMENT ON COLUMN sows_performance.cull_rate_boars IS '%';
COMMENT ON COLUMN sows_performance.fraction_own_replacement IS '%';
COMMENT ON COLUMN sows_performance.annual_sow_mortality IS '%';
COMMENT ON COLUMN sows_performance.annual_boar_mortality IS '%';
COMMENT ON COLUMN sows_performance.piglet_mortality_weaning IS '%';
COMMENT ON COLUMN sows_performance.piglet_mortality_rearing IS '%';
COMMENT ON COLUMN sows_performance.piglets_weaned IS 'piglets/sow/year';
COMMENT ON COLUMN sows_performance.avg_duration_piglet_rearing IS 'days';
COMMENT ON COLUMN sows_performance.reared_piglets IS 'piglets/sow/year';


CREATE TABLE "liabilities_interest_rates" (
	"id" uuid NOT NULL UNIQUE,
	"liabilities_id" uuid NOT NULL UNIQUE,
	-- %
	"long_term_loans" decimal(5,4),
	-- %
	"medium_term_loans" decimal(5,4),
	-- %
	"short_term_loans" decimal(5,4),
	-- %
	"circulating_capital_overdraft" decimal(5,4),
	-- %
	"savings" decimal(5,4),
	-- C
	"total_liabilities" decimal,
	-- C
	"total_long_term_loans" decimal,
	-- C
	"total_medium_term_loans" decimal,
	-- C
	"total_short_term_loans" decimal,
	-- %
	"perc_debt_total_assets" decimal(5,4),
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("liabilities_id")
);
COMMENT ON COLUMN liabilities_interest_rates.long_term_loans IS '%';
COMMENT ON COLUMN liabilities_interest_rates.medium_term_loans IS '%';
COMMENT ON COLUMN liabilities_interest_rates.short_term_loans IS '%';
COMMENT ON COLUMN liabilities_interest_rates.circulating_capital_overdraft IS '%';
COMMENT ON COLUMN liabilities_interest_rates.savings IS '%';
COMMENT ON COLUMN liabilities_interest_rates.total_liabilities IS 'C';
COMMENT ON COLUMN liabilities_interest_rates.total_long_term_loans IS 'C';
COMMENT ON COLUMN liabilities_interest_rates.total_medium_term_loans IS 'C';
COMMENT ON COLUMN liabilities_interest_rates.total_short_term_loans IS 'C';
COMMENT ON COLUMN liabilities_interest_rates.perc_debt_total_assets IS '%';


CREATE TABLE "overhead_costs" (
	"id" uuid NOT NULL UNIQUE,
	"overhead_id" uuid NOT NULL UNIQUE,
	-- Drainage etc.;C/year
	"land_improvements" decimal,
	-- If not known, calculate proxy, e.g. 3 % of the purchase price per annum; avoid double counting!;C/year
	"maintenance_machinery" decimal,
	-- If not known, calculate proxy, e.g. 1,5 % of the purchase price per annum; avoid double counting!;C/year
	"maintenance_buildings" decimal,
	-- C/year
	"contracted_labour_machinery_association" decimal,
	-- Includes Pick-up trucks, farm vehicles, NOT tractors for crop and forage production (var. cost per ha!);C/year
	"diesel_vehicles" decimal,
	-- C/year
	"diesel_heating_irrigation" decimal,
	-- C/year
	"gasoline" decimal,
	-- C/year
	"gas" decimal,
	-- C/year
	"electricity" decimal,
	-- Water and energy for the farmstead, not for crop production and other enterprises	;C/year
	"water_fresh_waste_water_fees" decimal,
	-- Insurances to cover the farm, e.g. fire insurance, crop insurance under other variable cost crop;C/year
	"farm_insurance" decimal,
	-- Fees for institutions that provide accident insurances and check safety on the farms;C/year	
	"invalidity_insurance" decimal,
	-- Only farm taxes like ground tax, no personal taxes like income tax!;C/year
	"taxes_fees" decimal,
	-- Costs for advisory/extension services if it cannot be allocated to the enterprises;C/year
	"advisory_services_trainings" decimal,
	-- E.g. costs for hiring a person or a company to do the accounting;C/year
	"accounting" decimal,
	-- All kind of materials, hardware and communication expenses;C/year		
	"office_communication_subs" decimal,
	-- C/year
	"others" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("overhead_id")
);
COMMENT ON COLUMN overhead_costs.land_improvements IS 'Drainage etc.;C/year';
COMMENT ON COLUMN overhead_costs.maintenance_machinery IS 'If not known, calculate proxy, e.g. 3 % of the purchase price per annum; avoid double counting!;C/year';
COMMENT ON COLUMN overhead_costs.maintenance_buildings IS 'If not known, calculate proxy, e.g. 1,5 % of the purchase price per annum; avoid double counting!;C/year';
COMMENT ON COLUMN overhead_costs.contracted_labour_machinery_association IS 'C/year';
COMMENT ON COLUMN overhead_costs.diesel_vehicles IS 'Includes Pick-up trucks, farm vehicles, NOT tractors for crop and forage production (var. cost per ha!);C/year';
COMMENT ON COLUMN overhead_costs.diesel_heating_irrigation IS 'C/year';
COMMENT ON COLUMN overhead_costs.gasoline IS 'C/year';
COMMENT ON COLUMN overhead_costs.gas IS 'C/year';
COMMENT ON COLUMN overhead_costs.electricity IS 'C/year';
COMMENT ON COLUMN overhead_costs.water_fresh_waste_water_fees IS 'Water and energy for the farmstead, not for crop production and other enterprises	;C/year';
COMMENT ON COLUMN overhead_costs.farm_insurance IS 'Insurances to cover the farm, e.g. fire insurance, crop insurance under other variable cost crop;C/year';
COMMENT ON COLUMN overhead_costs.invalidity_insurance IS 'Fees for institutions that provide accident insurances and check safety on the farms;C/year	';
COMMENT ON COLUMN overhead_costs.taxes_fees IS 'Only farm taxes like ground tax, no personal taxes like income tax!;C/year';
COMMENT ON COLUMN overhead_costs.advisory_services_trainings IS 'Costs for advisory/extension services if it cannot be allocated to the enterprises;C/year';
COMMENT ON COLUMN overhead_costs.accounting IS 'E.g. costs for hiring a person or a company to do the accounting;C/year';
COMMENT ON COLUMN overhead_costs.office_communication_subs IS 'All kind of materials, hardware and communication expenses;C/year		';
COMMENT ON COLUMN overhead_costs.others IS 'C/year';


CREATE TABLE "direct_aid_from_farm" (
	"id" uuid NOT NULL UNIQUE,
	"direct_aid_id" uuid NOT NULL UNIQUE,
	-- C/year
	"compensatory_allovance_disadvantage_area" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("direct_aid_id")
);
COMMENT ON COLUMN direct_aid_from_farm.compensatory_allovance_disadvantage_area IS 'C/year';


CREATE TABLE "acerage_prices" (
	"id" uuid NOT NULL UNIQUE,
	"acerage_id" uuid NOT NULL UNIQUE,
	-- Cropland	Grassland	Other incl. wood
	"land_type" varchar(50),
	-- ha
	"own_land" decimal,
	-- ha
	"rented_land" decimal,
	-- C/ha
	"rent_existing_contracts" decimal,
	-- C/ha
	"rent_new_contracts" decimal,
	-- C/ha
	"market_value" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("acerage_id")
);
COMMENT ON COLUMN acerage_prices.land_type IS 'Cropland	Grassland	Other incl. wood';
COMMENT ON COLUMN acerage_prices.own_land IS 'ha';
COMMENT ON COLUMN acerage_prices.rented_land IS 'ha';
COMMENT ON COLUMN acerage_prices.rent_existing_contracts IS 'C/ha';
COMMENT ON COLUMN acerage_prices.rent_new_contracts IS 'C/ha';
COMMENT ON COLUMN acerage_prices.market_value IS 'C/ha';


CREATE TABLE "land_use" (
	"id" uuid NOT NULL UNIQUE,
	"landuse_id" uuid NOT NULL UNIQUE,
	-- Set aside, Corn, Wheat, Barley
	"crop_name" varchar(50),
	-- ha
	"acerage" decimal,
	-- t/ha
	"net_yield" decimal,
	-- 0,0x
	"dry_matter" decimal,
	-- C/t
	"price" decimal,
	-- C/ha
	"cap_dir_paym" decimal,
	-- C/ha
	"other_dir_paym" decimal,
	"enterprise_code" int,
	"crop_id" uuid,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("landuse_id")
);
COMMENT ON COLUMN land_use.crop_name IS 'Set aside, Corn, Wheat, Barley';
COMMENT ON COLUMN land_use.acerage IS 'ha';
COMMENT ON COLUMN land_use.net_yield IS 't/ha';
COMMENT ON COLUMN land_use.dry_matter IS '0,0x';
COMMENT ON COLUMN land_use.price IS 'C/t';
COMMENT ON COLUMN land_use.cap_dir_paym IS 'C/ha';
COMMENT ON COLUMN land_use.other_dir_paym IS 'C/ha';


CREATE TABLE "var_cost_crop" (
	"id" uuid NOT NULL UNIQUE,
	"var_cost_crop_id" uuid NOT NULL UNIQUE,
	-- Set aside, Corn, Wheat, Barley
	"crop_name" varchar(50),
	-- C/ha
	"seeds" decimal,
	-- C/ha
	"fertilizer" decimal,
	-- C/ha
	"herbicides" decimal,
	-- C/ha
	"fungicide" decimal,
	-- C/ha
	"contract_labor" decimal,
	-- C/ha
	"energy" decimal,
	-- C/ha
	"other" decimal,
	"crop_id" uuid,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("var_cost_crop_id")
);
COMMENT ON COLUMN var_cost_crop.crop_name IS 'Set aside, Corn, Wheat, Barley';
COMMENT ON COLUMN var_cost_crop.seeds IS 'C/ha';
COMMENT ON COLUMN var_cost_crop.fertilizer IS 'C/ha';
COMMENT ON COLUMN var_cost_crop.herbicides IS 'C/ha';
COMMENT ON COLUMN var_cost_crop.fungicide IS 'C/ha';
COMMENT ON COLUMN var_cost_crop.contract_labor IS 'C/ha';
COMMENT ON COLUMN var_cost_crop.energy IS 'C/ha';
COMMENT ON COLUMN var_cost_crop.other IS 'C/ha';


CREATE TABLE "feed_prices_dry_matter" (
	"id" uuid NOT NULL UNIQUE,
	"feed_prices_id" uuid NOT NULL UNIQUE,
	-- Bought-in forage, Minerals, Concentrates, Milk replacer ,Oils, Finishing Feed I, Finishing Feed II, Finishing , Feed III, Finishing Feed IV, Gestation feed, Lactation feed, Special gilt feed, Special boar feed, Piglet feed I, Piglet feed II
	"feed_type" varchar(50),
	-- C/t
	"price_per_tonne" decimal,
	-- %
	"dry_matter_percent" decimal(5,4),
	"energy_mj" decimal,
	-- %
	"protein" decimal,
	"text" varchar(255),
	"concentrate" boolean,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("feed_prices_id")
);
COMMENT ON COLUMN feed_prices_dry_matter.feed_type IS 'Bought-in forage, Minerals, Concentrates, Milk replacer ,Oils, Finishing Feed I, Finishing Feed II, Finishing , Feed III, Finishing Feed IV, Gestation feed, Lactation feed, Special gilt feed, Special boar feed, Piglet feed I, Piglet feed II';
COMMENT ON COLUMN feed_prices_dry_matter.price_per_tonne IS 'C/t';
COMMENT ON COLUMN feed_prices_dry_matter.dry_matter_percent IS '%';
COMMENT ON COLUMN feed_prices_dry_matter.protein IS '%';


CREATE TABLE "sales_weight" (
	"id" uuid NOT NULL UNIQUE,
	"sales_weight_id" uuid NOT NULL UNIQUE,
	-- kg CW per head
	"sales_weight_sows" decimal,
	-- kg CW per head
	"sales_weight_boars" decimal,
	-- kg LW per head
	"sales_weight_weaning_piglet" decimal,
	-- kg LW per head
	"sales_weight_rearing_piglet" decimal,
	"general_id" uuid,
	"year" int,
	PRIMARY KEY("sales_weight_id")
);
COMMENT ON COLUMN sales_weight.sales_weight_sows IS 'kg CW per head';
COMMENT ON COLUMN sales_weight.sales_weight_boars IS 'kg CW per head';
COMMENT ON COLUMN sales_weight.sales_weight_weaning_piglet IS 'kg LW per head';
COMMENT ON COLUMN sales_weight.sales_weight_rearing_piglet IS 'kg LW per head';


CREATE TABLE "prices_sows" (
	"id" uuid NOT NULL UNIQUE,
	"prices_sows_id" uuid NOT NULL UNIQUE,
	-- C/head
	"buying_gilts" decimal,
	-- C/head
	"buying_boars" decimal,
	-- C/kg CW
	"selling_sow" decimal,
	-- C/kg CW
	"selling_boar" decimal,
	-- C/head
	"selling_weaning_piglet" decimal,
	-- C/head
	"selling_rearing_piglet" decimal,
	-- % 0,0x
	"proportion_weaned_pigs_sold" decimal,
	"no_weaned_pigs_sold" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("prices_sows_id")
);
COMMENT ON COLUMN prices_sows.buying_gilts IS 'C/head';
COMMENT ON COLUMN prices_sows.buying_boars IS 'C/head';
COMMENT ON COLUMN prices_sows.selling_sow IS 'C/kg CW';
COMMENT ON COLUMN prices_sows.selling_boar IS 'C/kg CW';
COMMENT ON COLUMN prices_sows.selling_weaning_piglet IS 'C/head';
COMMENT ON COLUMN prices_sows.selling_rearing_piglet IS 'C/head';
COMMENT ON COLUMN prices_sows.proportion_weaned_pigs_sold IS '% 0,0x';


CREATE TABLE "performance_pig_finishing" (
	"id" uuid NOT NULL UNIQUE,
	"performance_fin_id" uuid NOT NULL UNIQUE,
	-- kg LW per head
	"stalling_in_weight" decimal,
	-- kg LW per head
	"stalling_in_weight_em_ic_piglets" decimal,
	-- days
	"avg_duration_finishing_period" decimal,
	-- days
	"cleaning_days_cycle" decimal,
	-- days
	"days_without_animals_instable" decimal,
	-- %
	"mortality" decimal(5,4),
	-- kg LW per head
	"avg_selling_weight_gi_ba" decimal,
	"carcass_yield_gi_ba" decimal,
	-- %
	"lean_meat_from_gi_ba" decimal,
	-- 0,0x
	"index_points_autofom_gi_ba" decimal,
	-- kg LW per head
	"avg_selling_weight_em_ic" decimal,
	-- %
	"carcass_yield_em_ic" decimal(5,4),
	-- 0,0x
	"index_points_autofom_em_ic" decimal,
	-- 0,0x
	"avg_duration_finishing_period_em_ic" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("performance_fin_id")
);
COMMENT ON COLUMN performance_pig_finishing.stalling_in_weight IS 'kg LW per head';
COMMENT ON COLUMN performance_pig_finishing.stalling_in_weight_em_ic_piglets IS 'kg LW per head';
COMMENT ON COLUMN performance_pig_finishing.avg_duration_finishing_period IS 'days';
COMMENT ON COLUMN performance_pig_finishing.cleaning_days_cycle IS 'days';
COMMENT ON COLUMN performance_pig_finishing.days_without_animals_instable IS 'days';
COMMENT ON COLUMN performance_pig_finishing.mortality IS '%';
COMMENT ON COLUMN performance_pig_finishing.avg_selling_weight_gi_ba IS 'kg LW per head';
COMMENT ON COLUMN performance_pig_finishing.lean_meat_from_gi_ba IS '%';
COMMENT ON COLUMN performance_pig_finishing.index_points_autofom_gi_ba IS '0,0x';
COMMENT ON COLUMN performance_pig_finishing.avg_selling_weight_em_ic IS 'kg LW per head';
COMMENT ON COLUMN performance_pig_finishing.carcass_yield_em_ic IS '%';
COMMENT ON COLUMN performance_pig_finishing.index_points_autofom_em_ic IS '0,0x';
COMMENT ON COLUMN performance_pig_finishing.avg_duration_finishing_period_em_ic IS '0,0x';


CREATE TABLE "prices_finishing" (
	"id" uuid NOT NULL UNIQUE,
	"prices_fin_id" uuid NOT NULL UNIQUE,
	-- C/ kg LW
	"buying_f_castpiglets" decimal,
	-- C/ kg LW
	"buying_piglets_for_finishing" decimal,
	-- C/ kg CW
	"selling_finishing_pigs_gi_ba" decimal,
	-- C/ kg CW
	"selling_finishing_pigs_em_ic" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("prices_fin_id")
);
COMMENT ON COLUMN prices_finishing.buying_f_castpiglets IS 'C/ kg LW';
COMMENT ON COLUMN prices_finishing.buying_piglets_for_finishing IS 'C/ kg LW';
COMMENT ON COLUMN prices_finishing.selling_finishing_pigs_gi_ba IS 'C/ kg CW';
COMMENT ON COLUMN prices_finishing.selling_finishing_pigs_em_ic IS 'C/ kg CW';


CREATE TABLE "var_cost_finishing" (
	"id" uuid NOT NULL UNIQUE,
	"var_cost_fin_id" uuid NOT NULL UNIQUE,
	-- C/head
	"veterinary_medicine_supplies" decimal,
	-- C/head
	"disinfection" decimal,
	-- C/head
	"energy" decimal,
	-- C/head
	"water" decimal,
	-- C/head
	"manure_cost" decimal,
	-- C/head
	"transport_cost" decimal,
	-- C/head
	"specialised_pig_advisor" decimal,
	-- C/head
	"animal_disease_levy" decimal,
	-- C/head
	"carcass_disposal" decimal,
	-- C/head
	"maintenance" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("var_cost_fin_id")
);
COMMENT ON COLUMN var_cost_finishing.veterinary_medicine_supplies IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.disinfection IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.energy IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.water IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.manure_cost IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.transport_cost IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.specialised_pig_advisor IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.animal_disease_levy IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.carcass_disposal IS 'C/head';
COMMENT ON COLUMN var_cost_finishing.maintenance IS 'C/head';


CREATE TABLE "labor_alloc_sow_finishing" (
	"id" uuid NOT NULL UNIQUE,
	-- 0,0x
	"casual_labor_sow" decimal,
	-- 0,0x
	"family_labor_sow" decimal,
	-- 0,0x
	"casual_labor_finishing" decimal,
	-- 0,0x
	"family_labor_finishing" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("id")
);
COMMENT ON COLUMN labor_alloc_sow_finishing.casual_labor_sow IS '0,0x';
COMMENT ON COLUMN labor_alloc_sow_finishing.family_labor_sow IS '0,0x';
COMMENT ON COLUMN labor_alloc_sow_finishing.casual_labor_finishing IS '0,0x';
COMMENT ON COLUMN labor_alloc_sow_finishing.family_labor_finishing IS '0,0x';


CREATE TABLE "feeding_finishing" (
	"id" uuid NOT NULL UNIQUE,
	"feed_fin_id" uuid NOT NULL UNIQUE,
	-- %
	"proportion_finishing_feed_1" decimal(5,4),
	-- %
	"proportion_finishing_feed_2" decimal(5,4),
	"proportion_finishing_feed_3" decimal(5,4),
	-- kg/year
	"amount_finishing_feed_1" decimal,
	-- kg/year
	"amount_finishing_feed_2" decimal,
	-- kg/year
	"amount_finishing_feed_3" decimal,
	-- kg/year
	"total_amount_feed" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("feed_fin_id")
);
COMMENT ON COLUMN feeding_finishing.proportion_finishing_feed_1 IS '%';
COMMENT ON COLUMN feeding_finishing.proportion_finishing_feed_2 IS '%';
COMMENT ON COLUMN feeding_finishing.amount_finishing_feed_1 IS 'kg/year';
COMMENT ON COLUMN feeding_finishing.amount_finishing_feed_2 IS 'kg/year';
COMMENT ON COLUMN feeding_finishing.amount_finishing_feed_3 IS 'kg/year';
COMMENT ON COLUMN feeding_finishing.total_amount_feed IS 'kg/year';


CREATE TYPE "fertilizer_type_t" AS ENUM ('organic', 'mineral');

CREATE TYPE "fertilizer_name_t" AS ENUM ('nitrogen', 'phosphorus', 'potash', 'calcium', 'others');

CREATE TABLE "fertilizer" (
	"id" uuid NOT NULL UNIQUE,
	"fertilizer_id" uuid NOT NULL UNIQUE,
	"fertilizer_type" fertilizer_type_t,
	"fertilizer_name" fertilizer_name_t,
	"fertilizer_name_custom" varchar(255),
	"amount" decimal,
	"amount_unit" decimal,
	"n_content_per_unit" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	PRIMARY KEY("fertilizer_id")
);


CREATE TYPE "cereal_type_t" AS ENUM ('corn', 'wheat', 'barley', 'set-aside', 'bought-in forage', 'minerals', 'concentrates', 'milk replacer', 'oils');

CREATE TABLE "feeds" (
	"id" uuid NOT NULL UNIQUE,
	"cereal_type" cereal_type_t,
	"dry_matter" float,
	"xp" float,
	"energy" float,
	PRIMARY KEY("id")
);


CREATE TYPE "production_t" AS ENUM ('sows', 'finishing');

CREATE TYPE "feed_sources_t" AS ENUM ('Self produced', 'Bought feed');

CREATE TYPE "feed_type_t" AS ENUM ('Gestation feed', 'Lactation feed', 'Special gilt feed', 'Special boar feed', 'Piglet feed 1', 'Piglet feed 2', 'Finishing feed 1', 'Finishing feed 2', 'Finishing feed 3');

CREATE TABLE "feed_ration" (
	"id" uuid NOT NULL UNIQUE,
	"feed_ration_id" uuid NOT NULL UNIQUE,
	"production" production_t,
	"feed_sources" feed_sources_t,
	"feed_type" feed_type_t,
	"feed_share" decimal,
	"total_amount_feed_used" decimal,
	"general_id" uuid NOT NULL,
	"year" int,
	"feeds_id" uuid,
	PRIMARY KEY("feed_ration_id")
);


ALTER TABLE "feed_sows"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "sows"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "pig_finishing"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "cash_crops"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "cash_crops"
ADD FOREIGN KEY("feed_id") REFERENCES "feed_sows"("feed_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "labour"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "machines"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "machines"
ADD FOREIGN KEY("finishing_id") REFERENCES "pig_finishing"("finishing_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "machines"
ADD FOREIGN KEY("sow_id") REFERENCES "sows"("sows_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "labour"
ADD FOREIGN KEY("finishing_id") REFERENCES "pig_finishing"("finishing_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "labour"
ADD FOREIGN KEY("sow_id") REFERENCES "sows"("sows_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "buildings"
ADD FOREIGN KEY("finishing_id") REFERENCES "pig_finishing"("finishing_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "buildings"
ADD FOREIGN KEY("sow_id") REFERENCES "sows"("sows_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "feed_sows"
ADD FOREIGN KEY("finishing_id") REFERENCES "pig_finishing"("finishing_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "feed_sows"
ADD FOREIGN KEY("sow_id") REFERENCES "sows"("sows_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "buildings"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "feeding_finishing"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "land_use"
ADD FOREIGN KEY("crop_id") REFERENCES "cash_crops"("crops_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "var_cost_crop"
ADD FOREIGN KEY("crop_id") REFERENCES "cash_crops"("crops_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "liabilities_interest_rates"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "overhead_costs"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "direct_aid_from_farm"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "acerage_prices"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "land_use"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "var_cost_crop"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "feed_prices_dry_matter"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "variable_costs_sows"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "fix_costs"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "var_cost_finishing"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "sows_performance"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "sales_weight"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "prices_sows"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "prices_finishing"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "performance_pig_finishing"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "labor_alloc_sow_finishing"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "fertilizer"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "feed_ration"
ADD FOREIGN KEY("general_id") REFERENCES "general_farm"("general_id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "feed_ration"
ADD FOREIGN KEY("feeds_id") REFERENCES "feeds"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;