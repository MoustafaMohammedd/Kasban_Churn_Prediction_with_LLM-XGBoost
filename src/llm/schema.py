from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"


class SeniorCitizenEnum(str, Enum):
    yes = "Yes"
    no = "No"


class PartnerEnum(str, Enum):
    yes = "Yes"
    no = "No"


class DependentsEnum(str, Enum):
    yes = "Yes"
    no = "No"


class PhoneServiceEnum(str, Enum):
    yes = "Yes"
    no = "No"


class MultipleLinesEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_phone_service = "No phone service"


class InternetServiceEnum(str, Enum):
    fiber_optic = "Fiber optic"
    dsl = "DSL"
    no = "No"


class OnlineSecurityEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"


class OnlineBackupEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"


class DeviceProtectionEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"


class TechSupportEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"


class StreamingTVEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"


class StreamingMoviesEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"


class ContractEnum(str, Enum):
    month_to_month = "Month-to-month"
    one_year = "One year"
    two_year = "Two year"


class PaperlessBillingEnum(str, Enum):
    yes = "Yes"
    no = "No"


class PaymentMethodEnum(str, Enum):
    electronic_check = "Electronic check"
    mailed_check = "Mailed check"
    bank_transfer = "Bank transfer (automatic)"
    credit_card = "Credit card (automatic)"


class ClientFeatures(BaseModel):
    gender : GenderEnum = Field(description="Client gender: Male or Female")
    SeniorCitizen : SeniorCitizenEnum = Field(description="Is client a senior citizen (Yes/No)")
    Partner : PartnerEnum = Field(description="Does client have a partner (Yes/No)")
    Dependents : DependentsEnum = Field(description="Does client have dependents (Yes/No)")
    tenure : int = Field(description="Number of months the client has stayed")
    PhoneService : PhoneServiceEnum = Field(description="Does client have phone service (Yes/No)")
    MultipleLines : MultipleLinesEnum = Field(description="Multiple lines status")
    InternetService : InternetServiceEnum = Field(description="Type of internet service")
    OnlineSecurity : OnlineSecurityEnum = Field(description="Online security service")
    OnlineBackup : OnlineBackupEnum = Field(description="Online backup service")
    DeviceProtection : DeviceProtectionEnum = Field(description="Device protection service")
    TechSupport  : TechSupportEnum = Field(description="Tech support availability")
    StreamingTV : StreamingTVEnum = Field(description="Streaming TV subscription")
    StreamingMovies  : StreamingMoviesEnum = Field(description="Streaming movies subscription")
    Contract : ContractEnum = Field(description="Contract type")
    PaperlessBilling  : PaperlessBillingEnum = Field(description="Is paperless billing enabled")
    PaymentMethod  : PaymentMethodEnum = Field(description="Payment method")
    MonthlyCharges : float = Field(description="Monthly charges billed to the client")
    TotalCharges :  float = Field(description="Total charges billed to the client")
    
    
    # tenure: Optional[int] = Field(
    #     description="Number of months the customer has stayed with the company",
    #     default=None
    #         )
    # MonthlyCharges: Optional[float] = Field(
    #     description="Monthly charges billed to the client",
    #     default=None
    #         )
    # TotalCharges: Optional[float] = Field(
    #     description="Total charges billed to the client",
    #     default=None
    #         )

